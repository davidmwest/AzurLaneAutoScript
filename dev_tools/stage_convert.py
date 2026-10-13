"""
Convert stage modules under ./campaign into declarations in `campaign/<folder>/stages.py`,
see module/campaign/stage.py

A stage module is converted only when the classes built from its declaration are proven to be
the ones the module defines: same map, same config, and battle functions with the same syntax
tree. A stage with anything else in it keeps its module.

Usage:
    python -m dev_tools.stage_convert                       Report what can be converted.
    python -m dev_tools.stage_convert --write               Convert every folder.
    python -m dev_tools.stage_convert --write event_20250912_cn war_archives_20220224_cn

After merging upstream, run it with --write again. New and changed stage modules are converted,
and the declarations of untouched stages are kept.
"""
import argparse
import ast
import collections
import copy
import dataclasses
import importlib
import os
import re
import sys

from module.campaign.stage import (CAMPAIGN_FOLDER, DEFAULT_BASE, HELPER_MODULES, STAGES_MODULE, Stage, build_stage,
                                   render_plan)
from module.map.map_grids import SelectedGrids
from module.map_detection.grid_info import GridInfo

# Attributes of CampaignMap that hold a block of text parsed token by token,
# so their indentation is free to change
MAP_TEXT_BLOCKS = ('map_data', 'map_data_loop', 'weight_data')
MAP_ATTRS = MAP_TEXT_BLOCKS + (
    'shape', 'spawn_data', 'spawn_data_loop', 'camera_data', 'camera_data_spawn_point', 'camera_sight',
    'map_covered', 'wall_data', 'fortress_data', 'portal_data', 'bouncing_enemy_data', 'land_based_data',
    'maze_data', 'in_map_swipe_preset_data',
)
# Imports every stage module has, whatever it uses of them
BOILERPLATE_IMPORTS = {
    'module.logger:logger',
    'module.map.map_base:CampaignMap',
    'module.map.map_grids:RoadGrids',
    'module.map.map_grids:SelectedGrids',
}
GRID_NAME = re.compile(r'^[A-Z]{1,2}\d{1,2}$')
LITERAL_NODES = (
    ast.Expression, ast.Num, ast.Str, ast.Bytes, ast.NameConstant, ast.Constant, ast.Tuple, ast.List, ast.Dict,
    ast.Set, ast.Load, ast.UnaryOp, ast.USub, ast.UAdd, ast.BinOp, ast.Add, ast.Sub, ast.Mult, ast.Div,
)


class Unsupported(Exception):
    """The stage module has something a declaration cannot express."""


def literal(node):
    """
    Value of an expression made of literals and arithmetic on them, such as `(80, 255 - 17)`
    """
    for child in ast.walk(node):
        if not isinstance(child, LITERAL_NODES):
            raise Unsupported(f'not a literal: {type(child).__name__}')
    return eval(compile(ast.Expression(node), '<literal>', 'eval'), {'__builtins__': {}}, {})


def unparse(node):
    """
    Source of the expressions battle functions are made of. Python 3.7 has no ast.unparse.
    """
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return f'{unparse(node.value)}.{node.attr}'
    if isinstance(node, ast.Call):
        if any(isinstance(arg, ast.Starred) for arg in node.args) or any(kw.arg is None for kw in node.keywords):
            raise Unsupported('star arguments')
        args = [unparse(arg) for arg in node.args] + [f'{kw.arg}={unparse(kw.value)}' for kw in node.keywords]
        return f'{unparse(node.func)}({", ".join(args)})'
    if isinstance(node, ast.Tuple):
        items = [unparse(item) for item in node.elts]
        return f'({items[0]},)' if len(items) == 1 else f'({", ".join(items)})'
    if isinstance(node, ast.List):
        return f'[{", ".join(unparse(item) for item in node.elts)}]'
    return repr(literal(node))


def self_call(node):
    """
    Args:
        node: `self.clear_enemy(scale=(1,))`

    Returns:
        str: The step of a battle plan, 'clear_enemy(scale=(1,))'
    """
    if not isinstance(node, ast.Call):
        raise Unsupported('not a call')
    for name in [child.id for child in ast.walk(node) if isinstance(child, ast.Name)]:
        if name not in ('self', 'MAP') and not GRID_NAME.match(name):
            raise Unsupported(f'battle function uses `{name}`')
    text = unparse(node)
    if not text.startswith('self.'):
        raise Unsupported(f'not a call on self: {text}')
    text = text[len('self.'):]
    return text[:-2] if text.endswith('()') and not node.args and not node.keywords else text


def self_attribute(node):
    text = unparse(node)
    if isinstance(node, ast.Call) or not text.startswith('self.'):
        raise Unsupported(f'not an attribute of self: {text}')
    return text[len('self.'):]


def is_return_true(statements):
    if len(statements) != 1 or not isinstance(statements[0], ast.Return):
        return False
    value = statements[0].value
    return isinstance(value, (ast.NameConstant, ast.Constant)) and value.value is True


def is_docstring(node):
    return isinstance(node, ast.Expr) and isinstance(node.value, (ast.Str, ast.Constant))


def step_from(node):
    """
    A step that does not end the plan, see module/campaign/stage.py
    """
    if isinstance(node, ast.Expr):
        return ('do', self_call(node.value))
    if isinstance(node, ast.If) and is_return_true(node.body) and not node.orelse:
        return self_call(node.test)
    if isinstance(node, ast.If):
        step = ('when', self_attribute(node.test), [step_from(child) for child in node.body])
        if node.orelse:
            step += ([step_from(child) for child in node.orelse],)
        return step
    raise Unsupported(f'battle function has `{type(node).__name__}`')


def plan_from(function):
    """
    Args:
        function (ast.FunctionDef): `def battle_0(self): ...`

    Returns:
        str, list: Battle plan.
    """
    arguments = function.args
    if [arg.arg for arg in arguments.args] != ['self'] or arguments.vararg or arguments.kwarg \
            or arguments.kwonlyargs or function.decorator_list:
        raise Unsupported(f'{function.name} is not a plain method')
    body = [node for node in function.body if not is_docstring(node)]
    if not body:
        raise Unsupported(f'{function.name} is empty')
    *head, last = body
    steps = [step_from(node) for node in head]
    if isinstance(last, ast.Return) and last.value is not None:
        steps.append(self_call(last.value))
    elif isinstance(last, ast.If) and is_return_true(last.body) and not last.orelse:
        # Falls off the end instead of returning the call
        raise Unsupported(f'{function.name} ends with a try')
    else:
        steps.append(step_from(last))
    plan = steps[0] if len(steps) == 1 and isinstance(steps[0], str) else steps

    rendered = ast.parse(render_plan(function.name, plan)).body[0]
    original = copy.copy(function)
    original.body = body
    if ast.dump(rendered) != ast.dump(original):
        raise Unsupported(f'{function.name} does not render back to itself')
    return plan


def reference_from(module, level, name):
    return f'{"." * level}{module or ""}:{name}'


def stage_from_source(source):
    """
    Args:
        source (str): Source code of a stage module.

    Returns:
        Stage:

    Raises:
        Unsupported:
    """
    imported = {}
    map_data = None
    config = None
    config_base_name = None
    campaign = None

    for node in ast.parse(source).body:
        if is_docstring(node):
            continue
        if isinstance(node, ast.ImportFrom):
            for alias in node.names:
                imported[alias.asname or alias.name] = reference_from(node.module, node.level, alias.name)
            continue
        if isinstance(node, ast.ClassDef) and node.name == 'Config' and config is None:
            if len(node.bases) > 1 or node.keywords or node.decorator_list:
                raise Unsupported('Config is not a plain class')
            config_base_name = unparse(node.bases[0]) if node.bases else None
            config = {}
            for item in node.body:
                if isinstance(item, ast.Pass) or is_docstring(item):
                    continue
                if not isinstance(item, ast.Assign) or len(item.targets) != 1 \
                        or not isinstance(item.targets[0], ast.Name):
                    raise Unsupported('Config has more than attributes')
                config[item.targets[0].id] = literal(item.value)
            continue
        if isinstance(node, ast.ClassDef) and node.name == 'Campaign' and campaign is None:
            if len(node.bases) != 1 or node.keywords or node.decorator_list:
                raise Unsupported('Campaign is not a plain subclass')
            campaign = {'base': unparse(node.bases[0]), 'attrs': {}, 'battle': {}, 'enemy_filter': None}
            for item in node.body:
                if isinstance(item, ast.Pass) or is_docstring(item):
                    continue
                if isinstance(item, ast.FunctionDef):
                    matched = re.match(r'^battle_(\d+)$', item.name)
                    if not matched:
                        raise Unsupported(f'Campaign defines {item.name}()')
                    campaign['battle'][int(matched.group(1))] = plan_from(item)
                    continue
                if not isinstance(item, ast.Assign) or len(item.targets) != 1 \
                        or not isinstance(item.targets[0], ast.Name):
                    raise Unsupported('Campaign has more than attributes and battle functions')
                name = item.targets[0].id
                if name == 'MAP':
                    if not isinstance(item.value, ast.Name) or item.value.id != 'MAP':
                        raise Unsupported('Campaign.MAP is not the MAP of the module')
                elif name == 'ENEMY_FILTER':
                    campaign['enemy_filter'] = literal(item.value)
                else:
                    campaign['attrs'][name] = literal(item.value)
            continue
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target, value = node.targets[0], node.value
            if isinstance(target, ast.Name) and target.id == 'MAP' and map_data is None:
                if not isinstance(value, ast.Call) or unparse(value.func) != 'CampaignMap' or value.keywords \
                        or len(value.args) > 1:
                    raise Unsupported('MAP is not a CampaignMap')
                map_data = {'name': literal(value.args[0])} if value.args else {}
                continue
            if isinstance(target, ast.Attribute) and unparse(target.value) == 'MAP' and map_data is not None:
                if target.attr not in MAP_ATTRS or target.attr in map_data:
                    raise Unsupported(f'MAP.{target.attr}')
                map_data[target.attr] = literal(value)
                continue
            if isinstance(target, ast.Tuple) and isinstance(value, ast.Call) and unparse(value.func) == 'MAP.flatten':
                continue
        raise Unsupported(f'module has `{source.splitlines()[node.lineno - 1].strip()[:60]}`')

    if map_data is None or campaign is None:
        raise Unsupported('not a stage, no MAP or no Campaign')
    for name, reference in imported.items():
        if name not in (campaign['base'], config_base_name, 'Config') and reference not in BOILERPLATE_IMPORTS:
            raise Unsupported(f'imports {reference}')
    if campaign['base'] not in imported:
        raise Unsupported(f'Campaign base `{campaign["base"]}` is not imported')

    # Config is either a class of the module, or imported from another stage as is
    if config is None:
        config, config_base_name = {}, 'Config'
        if 'Config' not in imported:
            raise Unsupported('no Config')
    config_base = None
    if config_base_name is not None:
        if config_base_name not in imported:
            raise Unsupported(f'Config base `{config_base_name}` is not imported')
        config_base = imported[config_base_name]
        # `from .a1 import Config` is the Config of stage a1
        matched = re.match(r'^\.(\w+):Config$', config_base)
        if matched and matched.group(1) not in HELPER_MODULES:
            config_base = matched.group(1)

    return Stage(
        map=map_data,
        config=config,
        config_base=config_base,
        base=imported[campaign['base']],
        enemy_filter=campaign['enemy_filter'],
        attrs=campaign['attrs'],
        battle=campaign['battle'],
    )


"""
Proof that a declaration builds what the module defines
"""


def normalize(value):
    if isinstance(value, SelectedGrids):
        return [grid.location for grid in value]
    if isinstance(value, GridInfo):
        return ('grid', value.location)
    if isinstance(value, (list, tuple)):
        return type(value)(normalize(item) for item in value)
    if isinstance(value, dict):
        return {key: normalize(item) for key, item in value.items()}
    return value


def map_state(campaign_map):
    state = normalize({key: value for key, value in vars(campaign_map).items() if key != 'grids'})
    for attr in ('_' + name for name in MAP_TEXT_BLOCKS):
        state[attr] = [row.strip() for row in state[attr].strip().split('\n')]
    state['grids'] = {location: normalize(vars(grid)) for location, grid in campaign_map.grids.items()}
    return state


def inherited_state(cls):
    return {name: getattr(cls, name) for name in dir(cls) if not name.startswith('__')}


def own_state(cls, exclude=()):
    return {name: value for name, value in vars(cls).items() if not name.startswith('__') and name not in exclude}


def difference(folder, name, stage):
    """
    Returns:
        str: What the built stage has different from its module, empty if nothing.
    """
    module = importlib.import_module(f'campaign.{folder}.{name}')
    built = build_stage(folder, name, stage)
    if map_state(built.MAP) != map_state(module.MAP):
        return 'MAP'
    # The Config of a stage may inherit from the Config of another, which is a different class once built
    if inherited_state(built.Config) != inherited_state(module.Config):
        return 'Config'
    if built.Campaign.__bases__ != module.Campaign.__bases__:
        return 'Campaign bases'
    battles = [f'battle_{index}' for index in stage.battle]
    # Battle functions are proven by plan_from() already
    exclude = ['MAP'] + battles
    if own_state(built.Campaign, exclude) != own_state(module.Campaign, exclude):
        return 'Campaign attributes'
    if sorted(battles) != sorted(key for key in vars(module.Campaign) if key.startswith('battle_')):
        return 'Campaign battle functions'
    return ''


"""
Writing campaign/<folder>/stages.py
"""


def format_text_block(text, indent):
    rows = [row.strip() for row in text.strip().split('\n')]
    return '"""\n' + ''.join(f'{indent}    {row}\n' for row in rows) + f'{indent}"""'


def format_value(value, indent, lead=0):
    """
    repr() of a value, one item per line once it gets long.

    Args:
        value:
        indent (str): Indentation of the line the value starts on.
        lead (int): Length of what is on that line before the value, such as `name=`
    """
    text = repr(value)
    if len(indent) + lead + len(text) < 110 or not value:
        return text
    if isinstance(value, dict):
        items = [f'{indent}    {key!r}: {format_value(item, indent + "    ")},\n' for key, item in value.items()]
        return '{\n' + ''.join(items) + indent + '}'
    if isinstance(value, list):
        items = [f'{indent}    {format_value(item, indent + "    ")},\n' for item in value]
        return '[\n' + ''.join(items) + indent + ']'
    return text


def format_stage(stage, constants):
    """
    Args:
        stage (Stage):
        constants (dict): Value to the name of a constant of the stages module.

    Returns:
        str: `Stage(...)`
    """

    def shared(value, indent):
        return constants.get(repr(value)) or format_value(value, indent)

    lines = ['Stage(']
    if stage.base != DEFAULT_BASE:
        lines.append(f'        base={shared(stage.base, "        ")},')
    lines.append('        map=dict(')
    for attr, value in stage.map.items():
        if attr in MAP_TEXT_BLOCKS:
            value = format_text_block(value, indent='            ')
        elif attr == 'wall_data':
            # Parsed by column, keep it as it is
            value = '"""' + value + '"""'
        else:
            value = format_value(value, indent='            ')
        lines.append(f'            {attr}={value},')
    lines.append('        ),')
    if stage.config_base is not None:
        lines.append(f'        config_base={stage.config_base!r},')
    if stage.config:
        lines.append('        config=dict(')
        lines += [f'            {key}={format_value(value, "            ", lead=len(key) + 1)},'
                  for key, value in stage.config.items()]
        lines.append('        ),')
    if stage.enemy_filter is not None:
        lines.append(f'        enemy_filter={shared(stage.enemy_filter, "        ")},')
    if stage.attrs:
        lines.append(f'        attrs={format_value(stage.attrs, "        ")},')
    if stage.battle:
        lines.append('        battle={')
        lines += [f'            {index}: {shared(plan, "            ")},' for index, plan in sorted(stage.battle.items())]
        lines.append('        },')
    lines.append('    )')
    return '\n'.join(lines)


def format_stages(folder, stages, archived=None):
    """
    Args:
        folder (str):
        stages (dict[str, Stage]):
        archived (tuple[str, dict[str, Stage]]): Folder and stages of the event this folder archives, if it is
            a war archive. Stages that are the same there apart from their base are borrowed from it.

    Returns:
        str: Source code of campaign/<folder>/stages.py
    """
    borrow = collections.defaultdict(list)  # Change of base, or None: names
    if archived:
        for name, stage in stages.items():
            origin = archived[1].get(name)
            if origin and comparable(dataclasses.replace(origin, base=stage.base)) == comparable(stage):
                borrow[stage.base if stage.base != origin.base else None].append(name)
    borrowed_names = [name for names in borrow.values() for name in names]
    stages = {name: stage for name, stage in stages.items() if name not in borrowed_names}

    # Values most stages of an event share get a name
    usage = collections.Counter()
    for stage in stages.values():
        usage[('BASE', repr(stage.base))] += stage.base != DEFAULT_BASE
        usage[('ENEMY_FILTER', repr(stage.enemy_filter))] += stage.enemy_filter is not None
        for plan in stage.battle.values():
            usage[('PLAN', repr(plan))] += isinstance(plan, list)
    constants = {}
    for prefix in ('BASE', 'ENEMY_FILTER', 'PLAN'):
        ranked = [(count, value) for (kind, value), count in usage.items() if kind == prefix and count >= 2]
        for index, (_, value) in enumerate(sorted(ranked, reverse=True)):
            constants[value] = prefix if index == 0 else f'{prefix}_{index + 1}'

    imports = [name for name, used in (('Stage', stages), ('borrowed', borrow)) if used]
    lines = [
        '"""',
        f'Stages of {folder}, see module/campaign/stage.py',
        'Written by dev_tools/stage_convert.py',
        '"""',
    ]
    if borrow:
        lines.append(f'from campaign.{archived[0]}.{STAGES_MODULE} import STAGES as ARCHIVED')
    lines += [f'from module.campaign.stage import {", ".join(imports)}', '']
    lines += [f'{name} = {format_value(eval(value), "")}' for value, name in constants.items()]
    lines += ['', 'STAGES = {']
    for base, names in borrow.items():
        change = '' if base is None else f', base={base!r}'
        lines.append(f'    **borrowed(ARCHIVED, {format_value(names, "    ", lead=24)}{change}),')
    lines += [f'    {name!r}: {format_stage(stage, constants)},' for name, stage in stages.items()]
    lines += ['}', '']
    return '\n'.join(lines)


def comparable(stage):
    """
    A stage with the indentation of its text blocks taken out, which writing changes.
    """
    blocks = {attr: [row.strip() for row in stage.map[attr].strip().split('\n')]
              for attr in MAP_TEXT_BLOCKS if attr in stage.map}
    return dataclasses.replace(stage, map={**stage.map, **blocks})


"""
Converting folders
"""


def campaign_module(module, level, folder=None):
    """
    Args:
        module (str): Module of an import, 'campaign.event_20200326_cn.a1', or 'a1' at level 1
        level (int): Number of leading dots.
        folder (str): The campaign folder the import is in, if any.

    Returns:
        tuple[str, str]: (folder, name) if it is a module under ./campaign, or None
    """
    parts = module.split('.')
    if level == 0 and parts[0] == 'campaign' and len(parts) == 3:
        return parts[1], parts[2]
    if level == 1 and folder and len(parts) == 1:
        return folder, parts[0]
    if level == 2 and folder and len(parts) == 2:
        return parts[0], parts[1]
    return None


def imported_stages(path, folder=None):
    """
    Args:
        path (str): A python file.
        folder (str): The campaign folder it is in, if any.

    Returns:
        set[tuple[str, str]]: (folder, stage) of the stage modules it imports.
    """
    with open(path, encoding='utf-8') as f:
        source = f.read()
    found = set()
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.ImportFrom) and node.module:
            found.add(campaign_module(node.module, node.level, folder))
    # importlib.import_module('.' + name, 'campaign.campaign_main')
    for target in re.findall(r"import_module\([^)]*'campaign\.(\w+)'\)", source):
        found.add((target, '*'))
    found.discard(None)
    return found


def python_files(root):
    for folder, _, files in os.walk(root):
        for file in files:
            if file.endswith('.py'):
                yield os.path.join(folder, file)


def convert(folders, write=False):
    """
    Args:
        folders (list[str]): Folders under ./campaign
        write (bool): False to report only.
    """
    stages = {}  # (folder, name): Stage
    reasons = collections.Counter()
    kept = {}  # (folder, name): Why it keeps its module
    modules = {}  # (folder, name): path, of every module under ./campaign
    for folder in sorted(os.listdir(CAMPAIGN_FOLDER)):
        if not os.path.isdir(f'{CAMPAIGN_FOLDER}/{folder}'):
            continue
        for file in sorted(os.listdir(f'{CAMPAIGN_FOLDER}/{folder}')):
            name, ext = os.path.splitext(file)
            if ext == '.py':
                modules[(folder, name)] = f'{CAMPAIGN_FOLDER}/{folder}/{file}'

    declared = {}  # (folder, name): Stage, of the stages declared before
    for (folder, name), path in modules.items():
        if name == STAGES_MODULE:
            existing = importlib.import_module(f'campaign.{folder}.{STAGES_MODULE}').STAGES
            declared.update({(folder, stage_name): stage for stage_name, stage in existing.items()})
        if folder not in folders or name in HELPER_MODULES:
            continue
        with open(path, encoding='utf-8') as f:
            source = f.read()
        try:
            stages[(folder, name)] = stage_from_source(source)
        except Unsupported as e:
            kept[(folder, name)] = str(e)

    # A module that stays must still be able to import the modules it imports
    outside = set()
    for root in ('./module', './dev_tools', './submodule'):
        for path in python_files(root):
            outside |= imported_stages(path)
    while 1:
        pinned = set(outside)
        for (folder, name), path in modules.items():
            if (folder, name) not in stages:
                pinned |= imported_stages(path, folder)
        for (folder, name), stage in {**declared, **stages}.items():
            # References are imports too, `config_base='a1'` is not, load_stage() takes it either way
            for reference in (stage.base, stage.config_base or ''):
                module = reference.partition(':')[0] if ':' in reference else ''
                pinned.add(campaign_module(module.lstrip('.'), len(module) - len(module.lstrip('.')), folder))
        pinned = [key for key in stages if key in pinned or (key[0], '*') in pinned]
        if not pinned:
            break
        for key in pinned:
            del stages[key]
            kept[key] = 'imported by a module'

    for key, stage in list(stages.items()):
        try:
            wrong = difference(*key, stage)
        except Exception as e:
            wrong = f'{type(e).__name__}: {e}'
        if wrong:
            del stages[key]
            kept[key] = f'differs from its module in {wrong}'

    for reason in kept.values():
        reasons[re.sub(r'`.*`|\d+', '..', reason)] += 1
    total = len(stages) + len(kept)
    print(f'{len(stages)} of {total} stage modules can be declared')
    for reason, count in reasons.most_common():
        print(f'{count:6d}  kept: {reason}')

    if not write:
        return stages, kept

    def stages_of(folder):
        # A stage declared before stays declared, unless it has a module again that could not be converted
        return dict(sorted(
            (name, stage) for (stage_folder, name), stage in {**declared, **stages}.items()
            if stage_folder == folder and ((folder, name) in stages or (folder, name) not in modules)
        ))

    # Events before the war archives that borrow from them
    for folder in sorted(folders):
        in_folder = stages_of(folder)
        if not in_folder:
            continue
        archived = None
        if folder.startswith('war_archives_'):
            event = folder.replace('war_archives_', 'event_', 1)
            archived = (event, stages_of(event))
        file = f'{CAMPAIGN_FOLDER}/{folder}/{STAGES_MODULE}.py'
        source = format_stages(folder, in_folder, archived)
        written = {}
        exec(compile(source, file, 'exec'), written)
        if {name: comparable(stage) for name, stage in written['STAGES'].items()} \
                != {name: comparable(stage) for name, stage in in_folder.items()}:
            raise RuntimeError(f'{file} would not read back as it was written, nothing changed in {folder}')
        with open(file, 'w', encoding='utf-8', newline='') as f:
            f.write(source)
        # What borrows from this folder next must import what was just written
        sys.modules.pop(f'campaign.{folder}.{STAGES_MODULE}', None)
        importlib.invalidate_caches()
        for name in in_folder:
            if (folder, name) in stages:
                os.remove(modules[(folder, name)])
    print(f'Written, {len(stages)} stage modules removed')
    return stages, kept


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__.strip().split('\n')[0])
    parser.add_argument('folders', nargs='*', help='Folders under ./campaign, all of them by default')
    parser.add_argument('--write', action='store_true', help='Write stages.py and remove the converted modules')
    args = parser.parse_args()
    all_folders = sorted(f for f in os.listdir(CAMPAIGN_FOLDER) if os.path.isdir(f'{CAMPAIGN_FOLDER}/{f}'))
    unknown = [folder for folder in args.folders if folder not in all_folders]
    if unknown:
        sys.exit(f'No such folder under {CAMPAIGN_FOLDER}: {unknown}')
    convert(args.folders or all_folders, write=args.write)
