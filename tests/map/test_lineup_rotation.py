from types import SimpleNamespace
from unittest.mock import Mock, call

import pytest

from module.combat.level import Level
from module.map import lineup_rotation
from module.map.lineup_rotation import LineupRotation, lineup_slot, slots_to_rotate
from module.map.map_fleet_preparation import FleetPreparation


@pytest.mark.parametrize('lv_fleets, expected', [
    ({}, []),
    ({1: [119, 100, 1, 70, 119, 119]}, []),
    ({1: [120, 100, 1, 70, 119, 121]}, [(1, 0), (1, 5)]),
    # Unknown levels are left alone
    ({1: [-1] * 6, 2: [-1, 125, -1, -1, -1, -1]}, [(2, 1)]),
    ({2: [120] + [1] * 5, 1: [1] * 5 + [120]}, [(1, 5), (2, 0)]),
])
def test_slots_to_rotate(lv_fleets, expected):
    assert slots_to_rotate(lv_fleets, level=120) == expected


def test_lineup_slots_run_left_to_right_main_fleet_then_vanguard():
    slots = [lineup_slot(1, position) for position in range(6)]

    assert [slot.name for slot in slots] == [
        'FLEET_1_BACKLINE_1', 'FLEET_1_BACKLINE_2', 'FLEET_1_BACKLINE_3',
        'FLEET_1_VANGUARD_1', 'FLEET_1_VANGUARD_2', 'FLEET_1_VANGUARD_3',
    ]
    left_edges = [slot.button[0] for slot in slots]
    assert left_edges == sorted(left_edges)
    # The ship in the middle is half way between its neighbours
    assert slots[1].button[0] == (slots[0].button[0] + slots[2].button[0]) // 2
    # The second fleet is the row below
    assert lineup_slot(2, 0).button[1] > slots[0].button[1]
    assert lineup_slot(2, 0).button[0] == pytest.approx(slots[0].button[0], abs=2)


def test_levels_are_remembered_by_fleet():
    campaign = Level.__new__(Level)
    campaign.fleet_show_index = 1
    campaign.lv = [118, 119, 120, 100, 99, 98]
    campaign.lv_remember()
    campaign.fleet_show_index = 2
    campaign.lv = [70, 71, 72, 73, 74, 75]
    campaign.lv_remember()
    # A level that was not read does not wipe what is known
    campaign.fleet_show_index = 1
    campaign.lv = [119, 0, 120, 100, 99, 98]
    campaign.lv_remember()

    assert campaign.lv_fleets == {1: [119, 119, 120, 100, 99, 98], 2: [70, 71, 72, 73, 74, 75]}


def make_preparation(lv_fleets, enable=True, fleet_2=2):
    return SimpleNamespace(
        config=SimpleNamespace(ShipRotation_Enable=enable, ShipRotation_Level=120, Fleet_Fleet1=1, Fleet_Fleet2=fleet_2),
        device=SimpleNamespace(screenshot=Mock()),
        lv_fleets=lv_fleets,
        _rotation_failed=None,
    )


def rotation_returning(monkeypatch, replaced):
    rotation = SimpleNamespace(rotate=Mock(side_effect=replaced))
    monkeypatch.setattr(lineup_rotation, 'LineupRotation', Mock(return_value=rotation))
    return rotation


def test_ships_at_the_level_are_replaced_before_the_sortie(monkeypatch):
    rotation = rotation_returning(monkeypatch, [True, True])
    preparation = make_preparation({1: [120, 100, 100, 100, 100, 100], 2: [100, 100, 100, 100, 121, 100]})

    assert FleetPreparation.lineup_rotation(preparation) is True

    assert rotation.rotate.call_args_list == [call(1, 0), call(2, 4)]
    # The level of the ship that came in is not known yet
    assert preparation.lv_fleets == {1: [-1, 100, 100, 100, 100, 100], 2: [100, 100, 100, 100, -1, 100]}
    preparation.device.screenshot.assert_called_once_with()


def test_a_ship_that_can_not_be_replaced_is_not_tried_before_every_sortie(monkeypatch):
    rotation = rotation_returning(monkeypatch, [False])
    preparation = make_preparation({1: [120, 100, 100, 100, 100, 100]})

    assert FleetPreparation.lineup_rotation(preparation) is False
    assert FleetPreparation.lineup_rotation(preparation) is False

    assert rotation.rotate.call_count == 1


def test_nothing_is_done_without_rotation_or_without_a_ship_at_the_level(monkeypatch):
    rotation = rotation_returning(monkeypatch, [])

    assert FleetPreparation.lineup_rotation(make_preparation({1: [125] * 6}, enable=False)) is False
    assert FleetPreparation.lineup_rotation(make_preparation({1: [119] * 6})) is False
    # A fleet that is not used is left as it is
    assert FleetPreparation.lineup_rotation(make_preparation({2: [125] * 6}, fleet_2=0)) is False

    rotation.rotate.assert_not_called()


def make_rotation(candidates):
    return SimpleNamespace(
        ship_info_enter=Mock(),
        rotation_candidates=Mock(return_value=candidates),
        dock_select_one=Mock(),
        dock_select_confirm=Mock(),
        dock_reset=Mock(),
        ui_back=Mock(),
    )


def test_rotate_brings_in_the_first_ship_of_the_dock_that_fits():
    first, second = SimpleNamespace(level=118, button='CARD_2'), SimpleNamespace(level=117, button='CARD_3')
    rotation = make_rotation([first, second])

    assert LineupRotation.rotate(rotation, fleet=1, position=4) is True

    assert rotation.ship_info_enter.call_args[1]['click_button'].name == 'FLEET_1_VANGUARD_2'
    rotation.dock_select_one.assert_called_once_with('CARD_2')
    rotation.dock_select_confirm.assert_called_once()
    rotation.ui_back.assert_not_called()


def test_rotate_leaves_the_lineup_as_it_is_if_no_ship_fits():
    rotation = make_rotation([])

    assert LineupRotation.rotate(rotation, fleet=2, position=0) is False

    rotation.dock_select_one.assert_not_called()
    rotation.dock_select_confirm.assert_not_called()
    rotation.ui_back.assert_called_once()
