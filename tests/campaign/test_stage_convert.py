import sys
from dataclasses import replace
from types import SimpleNamespace

import pytest

from dev_tools.stage_convert import Unsupported, comparable, format_stages, stage_from_source
from module.campaign.stage import Stage

HEAD = '''
from .campaign_base import CampaignBase
from module.map.map_base import CampaignMap
from module.map.map_grids import SelectedGrids, RoadGrids
from module.logger import logger
from .d1 import Config as ConfigBase

MAP = CampaignMap('D3')
MAP.shape = 'C2'
MAP.camera_data = ['B1']
MAP.map_data = """
    SP -- ME
    -- ++ MB
"""
MAP.spawn_data = [
    {'battle': 0, 'enemy': 2, 'siren': 2},
    {'battle': 1, 'boss': 1},
]
A1, B1, C1, \\
A2, B2, C2, \\
    = MAP.flatten()


class Config(ConfigBase):
    # ===== Start of generated config =====
    MAP_SIREN_TEMPLATE = ['BlackDragonBoss02']
    MOVABLE_ENEMY_TURN = (2,)
    # ===== End of generated config =====
    INTERNAL_LINES_FIND_PEAKS_PARAMETERS = {
        'height': (80, 255 - 17),
    }
'''
CAMPAIGN = '''

class Campaign(CampaignBase):
    MAP = MAP
    ENEMY_FILTER = '1L > 1M'
    MAP_AIR_RAID_OVERLAY_TRANSPARENCY_THRESHOLD = 0.35

    def battle_0(self):
        """Clear what is in the way."""
        if self.clear_siren():
            return True
        if self.clear_filter_enemy(self.ENEMY_FILTER, preserve=1):
            return True

        return self.battle_default()

    def battle_1(self):
        return self.fleet_boss.clear_boss()
'''


def campaign_with(battle):
    """
    Source of a stage module whose Campaign has one battle function with this body.
    """
    body = ''.join(f'        {line}\n' for line in battle.strip().split('\n'))
    return HEAD + '\n\nclass Campaign(CampaignBase):\n    MAP = MAP\n\n    def battle_0(self):\n' + body


def test_stage_from_source():
    stage = stage_from_source(HEAD + CAMPAIGN)

    assert stage == Stage(
        base='.campaign_base:CampaignBase',
        map=dict(
            name='D3',
            shape='C2',
            camera_data=['B1'],
            map_data='\n    SP -- ME\n    -- ++ MB\n',
            spawn_data=[{'battle': 0, 'enemy': 2, 'siren': 2}, {'battle': 1, 'boss': 1}],
        ),
        config=dict(
            MAP_SIREN_TEMPLATE=['BlackDragonBoss02'],
            MOVABLE_ENEMY_TURN=(2,),
            INTERNAL_LINES_FIND_PEAKS_PARAMETERS={'height': (80, 238)},
        ),
        config_base='d1',
        enemy_filter='1L > 1M',
        attrs=dict(MAP_AIR_RAID_OVERLAY_TRANSPARENCY_THRESHOLD=0.35),
        battle={
            0: ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default'],
            1: 'fleet_boss.clear_boss',
        },
    )


@pytest.mark.parametrize('battle, plan', [
    ('return self.clear_boss()', 'clear_boss'),
    ('self.fleet_boss.capture_clear_boss()', [('do', 'fleet_boss.capture_clear_boss')]),
    ('self.clear_all_mystery()\nreturn self.battle_default()', [('do', 'clear_all_mystery'), 'battle_default']),
    ("if self.clear_enemy(scale=(2,), genre=['light', 'main']):\n    return True\nreturn self.battle_default()",
     ["clear_enemy(scale=(2,), genre=['light', 'main'])", 'battle_default']),
    ('if self.clear_chosen_enemy(C1, expected="siren"):\n    return True\nreturn self.battle_default()',
     ["clear_chosen_enemy(C1, expected='siren')", 'battle_default']),
    ('if self.map_is_clear_mode:\n    if self.clear_siren():\n        return True\n'
     "else:\n    if self.clear_any_enemy(sort=('cost_2',)):\n        return True\n"
     'return self.battle_default()',
     [('when', 'map_is_clear_mode', ['clear_siren'], ["clear_any_enemy(sort=('cost_2',))"]), 'battle_default']),
    ('if self.config.MAP_HAS_SIREN:\n    self.clear_all_mystery()\nreturn self.battle_default()',
     [('when', 'config.MAP_HAS_SIREN', [('do', 'clear_all_mystery')]), 'battle_default']),
])
def test_battle_plans(battle, plan):
    assert stage_from_source(campaign_with(battle)).battle == {0: plan}


@pytest.mark.parametrize('battle', [
    # Uses a name of the module
    'if self.clear_roadblocks([road_main]):\n    return True\nreturn self.battle_default()',
    # Falls off the end where a plan would return the call
    'if self.clear_siren():\n    return True',
    'return True',
    'boss = self.map.select(is_boss=True)\nreturn self.clear_boss()',
    'if not self.map_is_clear_mode:\n    self.clear_all_mystery()\nreturn self.battle_default()',
    'logger.info("boss")\nreturn self.clear_boss()',
    'return self.clear_boss(*self.args)',
])
def test_battle_functions_a_plan_cannot_express(battle):
    with pytest.raises(Unsupported):
        stage_from_source(campaign_with(battle))


@pytest.mark.parametrize('source', [
    HEAD,  # No Campaign
    HEAD.replace('MAP.spawn_data', 'road_main = RoadGrids([A1])\nMAP.spawn_data') + CAMPAIGN,
    HEAD.replace("MAP.camera_data = ['B1']", 'MAP.camera_data = [B1]') + CAMPAIGN,
    HEAD.replace('MAP.shape', 'MAP.grid_class') + CAMPAIGN,
    HEAD + CAMPAIGN + '\n    def map_data_init(self, map_):\n        super().map_data_init(map_)\n',
    HEAD + CAMPAIGN.replace('def battle_1(self)', '@Config.when(MAP_HAS_SIREN=True)\n    def battle_1(self)'),
    HEAD.replace('from module.logger import logger', 'from module.base.timer import Timer') + CAMPAIGN,
    HEAD.replace('class Config(ConfigBase):', 'class Config(ConfigBase):\n    def f(self):\n        pass') + CAMPAIGN,
    HEAD + CAMPAIGN.replace('(CampaignBase)', '(CampaignBaseT)'),
])
def test_modules_a_declaration_cannot_express(source):
    with pytest.raises(Unsupported):
        stage_from_source(source)


def test_config_imported_as_it_is():
    source = HEAD.replace('from .d1 import Config as ConfigBase', 'from .d1 import Config')
    source = source[:source.index('class Config')] + CAMPAIGN

    stage = stage_from_source(source)

    assert (stage.config, stage.config_base) == ({}, 'd1')


def test_config_base_that_is_not_a_stage():
    source = HEAD.replace('from .d1 import Config as ConfigBase', 'from .config_base import ConfigBase')

    assert stage_from_source(source + CAMPAIGN).config_base == '.config_base:ConfigBase'


def test_written_stages_read_back():
    stage = stage_from_source(HEAD + CAMPAIGN)
    stage.map['wall_data'] = '\n    ·   ·   ·\n      +---+\n'
    long = Stage(map=dict(stage.map, name='D2'), config=dict(STAGE_ENTRANCE=['half', '20240725'] * 12),
                 enemy_filter=stage.enemy_filter, battle=dict(stage.battle))
    stages = {'d3': stage, 'd2': long}

    source = format_stages('event_test', stages)
    written = {}
    exec(source, written)

    assert {name: comparable(s) for name, s in written['STAGES'].items()} \
        == {name: comparable(s) for name, s in stages.items()}
    # Shared values are named once
    assert source.count("'1L > 1M'") == 1
    assert source.count('clear_filter_enemy') == 1


def test_war_archive_borrows_the_stages_it_shares_with_its_event(monkeypatch):
    event = {name: stage_from_source(HEAD + CAMPAIGN) for name in ('a1', 'a2', 'sp')}
    war_archives_base = '..campaign_war_archives.campaign_base:CampaignBase'
    archive = {
        'a1': replace(event['a1'], base=war_archives_base),
        'a2': event['a2'],
        # The archive has a map of its own for this one
        'sp': replace(event['sp'], base=war_archives_base, map=dict(event['sp'].map, shape='D2')),
    }

    source = format_stages('war_archives_test', archive, archived=('event_test', event))
    monkeypatch.setitem(sys.modules, 'campaign.event_test.stages', SimpleNamespace(STAGES=event))
    written = {}
    exec(source, written)

    assert {name: comparable(s) for name, s in written['STAGES'].items()} \
        == {name: comparable(s) for name, s in archive.items()}
    assert "**borrowed(ARCHIVED, ['a1'], base='..campaign_war_archives.campaign_base:CampaignBase')," in source
    assert "**borrowed(ARCHIVED, ['a2'])," in source
    assert source.count('Stage(') == 1
