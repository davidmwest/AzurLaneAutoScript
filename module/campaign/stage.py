"""
Stages as data.

A stage used to be a module of its own: imports, a CampaignMap filled in line by line, the grid
names unpacked, a Config class, and a Campaign class whose battle functions repeat across
thousands of files. An event now declares its stages in one `campaign/<event>/stages.py`:

    STAGES = {
        'd3': Stage(
            map=dict(name='D3', shape='K9', map_data='...', spawn_data=[...]),
            config=dict(MAP_HAS_SIREN=True, ...),
            config_base='d1',
            enemy_filter='1L > 1M > 1E > 1C > 2L > 2M > 2E > 2C > 3L > 3M > 3E > 3C',
            battle={
                0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default'],
                6: 'fleet_boss.clear_boss',
            },
        ),
    }

and `load_stage()` builds the Config and Campaign classes that module used to define.

A stage that needs real code keeps a module of its own, `campaign/<event>/<stage>.py`, and
`load_stage()` prefers it. That is also how events merged from upstream work before they are
converted with `dev_tools/stage_convert.py`.

Battle plans:
    A plan is one step or a list of steps, and becomes a `battle_N(self)` method.
        'clear_siren'               Try it: `if self.clear_siren(): return True`.
                                    As the last step of a plan: `return self.clear_siren()`.
        'clear_enemy(scale=(1,))'   Same, with arguments. Evaluated with the grid names in scope.
        ('do', 'clear_all_mystery') Run it and carry on: `self.clear_all_mystery()`.
        ('when', 'map_is_clear_mode', [steps], [steps])
                                    `if self.map_is_clear_mode: ... else: ...`, the else branch is
                                    optional. Steps inside a branch never end the plan.
"""
import importlib
import linecache
import os
import types
from dataclasses import dataclass, field, replace

from module.base.utils import location2node
from module.map.map_base import CampaignMap

CAMPAIGN_FOLDER = './campaign'
STAGES_MODULE = 'stages'
# Modules in an event folder that are not stages
HELPER_MODULES = (STAGES_MODULE, 'campaign_base', 'config_base')
DEFAULT_BASE = 'module.campaign.campaign_base:CampaignBase'


@dataclass
class Stage:
    # Attributes of CampaignMap, set in this order. `name` goes to its constructor.
    map: dict
    # Attributes of the Config class
    config: dict = field(default_factory=dict)
    # Where Config inherits from, a stage of the same event such as 'a1', or a reference
    config_base: str = None
    # Where Campaign inherits from, a reference
    base: str = DEFAULT_BASE
    enemy_filter: str = None
    # Other attributes of the Campaign class
    attrs: dict = field(default_factory=dict)
    # Battle index to plan
    battle: dict = field(default_factory=dict)


def borrowed(stages, names, **changes):
    """
    Stages another event declares, with some of their fields changed.
    A war archive has the stages of the event it archives, on the base class of war archives.

    Args:
        stages (dict[str, Stage]): STAGES of the other event.
        names (list[str]):
        **changes: Fields of Stage.

    Returns:
        dict[str, Stage]:
    """
    return {name: replace(stages[name], **changes) for name in names}


class StageNotFound(Exception):
    pass


def _resolve(reference, package):
    """
    Args:
        reference (str): 'module.path:Name', a leading dot makes the module relative to `package`,
            such as '.campaign_base:CampaignBase'
        package (str): Such as 'campaign.event_20250912_cn'
    """
    module, _, name = reference.partition(':')
    module = importlib.import_module(module, package=package if module.startswith('.') else None)
    return getattr(module, name)


def _call(expr):
    return f'self.{expr}' if expr.endswith(')') else f'self.{expr}()'


def _render_steps(steps, indent, is_plan):
    lines = []
    for index, step in enumerate(steps):
        if isinstance(step, str):
            if is_plan and index == len(steps) - 1:
                lines.append(f'{indent}return {_call(step)}')
            else:
                lines.append(f'{indent}if {_call(step)}:')
                lines.append(f'{indent}    return True')
        elif step[0] == 'do':
            lines.append(f'{indent}{_call(step[1])}')
        elif step[0] == 'when':
            lines.append(f'{indent}if self.{step[1]}:')
            lines += _render_steps(step[2], indent + '    ', is_plan=False)
            if len(step) > 3:
                lines.append(f'{indent}else:')
                lines += _render_steps(step[3], indent + '    ', is_plan=False)
        else:
            raise ValueError(f'Unknown battle plan step: {step!r}')
    return lines


def render_plan(name, plan):
    """
    Args:
        name (str): Method name, such as 'battle_0'
        plan (str, tuple, list): See module docstring.

    Returns:
        str: Source code of the method.
    """
    steps = plan if isinstance(plan, list) else [plan]
    return '\n'.join([f'def {name}(self):'] + _render_steps(steps, indent='    ', is_plan=True)) + '\n'


def _compile_plan(name, plan, namespace, filename):
    source = render_plan(name, plan)
    # Tracebacks show the rendered source
    linecache.cache[filename] = (len(source), None, source.splitlines(True), filename)
    scope = {}
    exec(compile(source, filename, 'exec'), namespace, scope)
    return scope[name]


def build_stage(folder, name, stage):
    """
    Args:
        folder (str): Such as 'event_20250912_cn'
        name (str): Such as 'd3'
        stage (Stage):

    Returns:
        types.SimpleNamespace: What the module of a stage has, `MAP`, `Config` and `Campaign`.
    """
    package = f'campaign.{folder}'
    module_name = f'{package}.{name}'

    map_data = dict(stage.map)
    campaign_map = CampaignMap(map_data.pop('name', None))
    for attr, value in map_data.items():
        setattr(campaign_map, attr, value)

    if stage.config_base is None:
        config_bases = ()
    elif ':' in stage.config_base:
        config_bases = (_resolve(stage.config_base, package),)
    else:
        config_bases = (load_stage(folder, stage.config_base).Config,)
    config = type('Config', config_bases, dict(stage.config, __module__=module_name))

    # What battle plans can refer to, same as in a stage module
    namespace = {location2node(grid.location): grid for grid in campaign_map}
    namespace['MAP'] = campaign_map

    attrs = {'__module__': module_name, 'MAP': campaign_map}
    if stage.enemy_filter is not None:
        attrs['ENEMY_FILTER'] = stage.enemy_filter
    attrs.update(stage.attrs)
    for index, plan in stage.battle.items():
        method = f'battle_{index}'
        attrs[method] = _compile_plan(method, plan, namespace, filename=f'<stage {folder}/{name} {method}>')
    campaign = type('Campaign', (_resolve(stage.base, package),), attrs)

    return types.SimpleNamespace(MAP=campaign_map, Config=config, Campaign=campaign)


def _declared_stages(folder):
    """
    Returns:
        dict[str, Stage]: Stages declared in campaign/<folder>/stages.py, empty if it has none.
    """
    if not os.path.exists(f'{CAMPAIGN_FOLDER}/{folder}/{STAGES_MODULE}.py'):
        return {}
    return importlib.import_module(f'campaign.{folder}.{STAGES_MODULE}').STAGES


def _module_stages(folder):
    """
    Returns:
        list[str]: Stages that have a module of their own.
    """
    path = f'{CAMPAIGN_FOLDER}/{folder}'
    if not os.path.isdir(path):
        return []
    names = [os.path.splitext(file) for file in os.listdir(path)]
    return [name for name, ext in names if ext == '.py' and name not in HELPER_MODULES]


def stage_names(folder):
    """
    Args:
        folder (str): Folder under ./campaign, such as 'event_20250912_cn'

    Returns:
        list[str]: Such as ['a1', 'a2', 'a3', 'sp']
    """
    names = _module_stages(folder)
    names += [name for name in _declared_stages(folder) if name not in names]
    return names


_stage_cache = {}


def load_stage(folder, name):
    """
    Args:
        folder (str): Folder under ./campaign, such as 'event_20250912_cn'
        name (str): Such as 'd3'

    Returns:
        A module or a namespace having `MAP`, `Config` and `Campaign`.

    Raises:
        StageNotFound:
    """
    key = (folder, name)
    if key in _stage_cache:
        return _stage_cache[key]

    if os.path.exists(f'{CAMPAIGN_FOLDER}/{folder}/{name}.py'):
        stage = importlib.import_module(f'campaign.{folder}.{name}')
    else:
        declared = _declared_stages(folder)
        if name not in declared:
            raise StageNotFound(f'campaign.{folder}.{name}')
        stage = build_stage(folder, name, declared[name])

    _stage_cache[key] = stage
    return stage
