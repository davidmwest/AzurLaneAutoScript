import os
from unittest.mock import Mock

import pytest

import module.campaign.stage as stage_module
from module.campaign.campaign_base import CampaignBase
from module.campaign.stage import Stage, StageNotFound, build_stage, load_stage, render_plan, stage_names

MAP = dict(
    name='A1',
    shape='C2',
    camera_data=['B1'],
    map_data="""
        SP -- ME
        -- ++ MB
    """,
    spawn_data=[{'battle': 0, 'enemy': 1}, {'battle': 1, 'boss': 1}],
)
STANDARD = ['clear_siren', 'clear_filter_enemy(self.ENEMY_FILTER, preserve=1)', 'battle_default']


@pytest.fixture
def declared(monkeypatch, tmp_path):
    """
    Stages declared in an event that has no module on disk.
    """
    stages = {}
    monkeypatch.setattr(stage_module, 'CAMPAIGN_FOLDER', str(tmp_path))
    monkeypatch.setattr(stage_module, '_declared_stages', lambda folder: stages)
    monkeypatch.setattr(stage_module, '_stage_cache', {})
    return stages


def test_render_plan_of_one_step():
    assert render_plan('battle_5', 'fleet_boss.clear_boss') == (
        'def battle_5(self):\n'
        '    return self.fleet_boss.clear_boss()\n'
    )


def test_render_plan_tries_steps_and_returns_the_last():
    assert render_plan('battle_0', STANDARD) == (
        'def battle_0(self):\n'
        '    if self.clear_siren():\n'
        '        return True\n'
        '    if self.clear_filter_enemy(self.ENEMY_FILTER, preserve=1):\n'
        '        return True\n'
        '    return self.battle_default()\n'
    )


def test_render_plan_do_and_when():
    plan = [
        ('do', 'clear_all_mystery'),
        ('when', 'map_is_clear_mode', ['clear_siren'], ["clear_any_enemy(sort=('cost_2',))"]),
        'battle_default',
    ]
    assert render_plan('battle_0', plan) == (
        'def battle_0(self):\n'
        '    self.clear_all_mystery()\n'
        '    if self.map_is_clear_mode:\n'
        '        if self.clear_siren():\n'
        '            return True\n'
        '    else:\n'
        "        if self.clear_any_enemy(sort=('cost_2',)):\n"
        '            return True\n'
        '    return self.battle_default()\n'
    )


def test_render_plan_rejects_unknown_step():
    with pytest.raises(ValueError):
        render_plan('battle_0', [('unless', 'clear_siren')])


def test_build_stage_makes_the_classes_of_a_stage_module():
    stage = Stage(map=MAP, config=dict(MAP_HAS_SIREN=True, MOVABLE_ENEMY_TURN=(2,)),
                  enemy_filter='1L > 1M', attrs=dict(MAP_ENEMY_SEARCHING_OVERLAY_TRANSPARENCY_THRESHOLD=0.7),
                  battle={0: STANDARD, 1: 'fleet_boss.clear_boss'})

    built = build_stage('event_test', 'a1', stage)

    assert built.MAP.name == 'A1'
    assert built.MAP.shape == (2, 1)
    assert built.MAP[(2, 1)].may_boss
    assert built.Config.MAP_HAS_SIREN is True
    assert built.Config.MOVABLE_ENEMY_TURN == (2,)
    assert built.Config.__bases__ == (object,)
    assert built.Campaign.__bases__ == (CampaignBase,)
    assert built.Campaign.__module__ == 'campaign.event_test.a1'
    assert built.Campaign.MAP is built.MAP
    assert built.Campaign.ENEMY_FILTER == '1L > 1M'
    assert built.Campaign.MAP_ENEMY_SEARCHING_OVERLAY_TRANSPARENCY_THRESHOLD == 0.7


def test_built_battle_function_stops_at_the_first_step_that_fights():
    built = build_stage('event_test', 'a1', Stage(map=MAP, enemy_filter='1L > 1M', battle={0: STANDARD}))
    campaign = Mock(ENEMY_FILTER='1L > 1M')
    campaign.clear_siren.return_value = False
    campaign.clear_filter_enemy.return_value = True

    assert built.Campaign.battle_0(campaign) is True

    campaign.clear_filter_enemy.assert_called_once_with('1L > 1M', preserve=1)
    campaign.battle_default.assert_not_called()


def test_built_battle_function_falls_back_to_the_last_step():
    built = build_stage('event_test', 'a1', Stage(map=MAP, battle={0: STANDARD}))
    campaign = Mock()
    campaign.clear_siren.return_value = False
    campaign.clear_filter_enemy.return_value = False

    assert built.Campaign.battle_0(campaign) is campaign.battle_default.return_value


def test_battle_plan_can_name_grids():
    built = build_stage('event_test', 'a1', Stage(map=MAP, battle={0: 'clear_chosen_enemy(C1)'}))
    campaign = Mock()

    built.Campaign.battle_0(campaign)

    campaign.clear_chosen_enemy.assert_called_once_with(built.MAP[(2, 0)])


def test_config_inherits_from_the_config_of_another_stage(declared):
    declared['a1'] = Stage(map=MAP, config=dict(MAP_HAS_SIREN=True, MAP_HAS_AMBUSH=False))
    declared['a2'] = Stage(map=MAP, config=dict(MAP_HAS_AMBUSH=True), config_base='a1')

    config = load_stage('event_test', 'a2').Config

    assert config.__bases__ == (load_stage('event_test', 'a1').Config,)
    assert (config.MAP_HAS_SIREN, config.MAP_HAS_AMBUSH) == (True, True)


def test_base_reference_can_be_relative_to_the_event():
    # campaign_war_archives is not an event with stages, but it has the base class of war archives
    built = build_stage('war_archives_test', 'a1',
                        Stage(map=MAP, base='..campaign_war_archives.campaign_base:CampaignBase'))

    from campaign.campaign_war_archives.campaign_base import CampaignBase as WarArchivesBase
    assert built.Campaign.__bases__ == (WarArchivesBase,)


def test_load_stage_raises_for_a_stage_that_is_not_declared(declared):
    with pytest.raises(StageNotFound):
        load_stage('event_test', 'a1')


def test_load_stage_prefers_a_module(declared, tmp_path, monkeypatch):
    declared['a1'] = Stage(map=MAP)
    os.makedirs(tmp_path / 'event_test')
    (tmp_path / 'event_test' / 'a1.py').write_text('')
    module = object()
    monkeypatch.setattr(stage_module.importlib, 'import_module', lambda name: module)

    assert load_stage('event_test', 'a1') is module


def test_stage_names_lists_modules_and_declarations_once(declared, tmp_path):
    declared.update(a1=Stage(map=MAP), a2=Stage(map=MAP))
    os.makedirs(tmp_path / 'event_test')
    for file in ('a1.py', 'sp.py', 'campaign_base.py', 'stages.py', 'notes.txt'):
        (tmp_path / 'event_test' / file).write_text('')

    assert sorted(stage_names('event_test')) == ['a1', 'a2', 'sp']


def test_stage_names_of_a_folder_that_does_not_exist(declared):
    assert stage_names('event_missing') == []


def test_every_stage_in_the_repository_loads():
    # They import their entrance button from module.campaign.assets, which no longer has it
    known_broken = {('event_20200227_cn', 'c2'), ('event_20200227_cn', 'd3'), ('event_20200312_cn', 'sp3')}
    folders = sorted(folder for folder in os.listdir('./campaign') if os.path.isdir(f'./campaign/{folder}'))
    failed = []
    count = 0
    for folder in folders:
        for name in stage_names(folder):
            if (folder, name) in known_broken:
                continue
            count += 1
            try:
                stage = load_stage(folder, name)
            except Exception as e:
                failed.append(f'{folder}/{name}: {type(e).__name__}: {e}')
                continue
            # Helpers such as campaign_15_base have no stage in them
            if hasattr(stage, 'Campaign') and hasattr(stage, 'MAP'):
                assert stage.Campaign.MAP is stage.MAP, f'{folder}/{name}'
    assert not failed, failed
    assert count > 1000
