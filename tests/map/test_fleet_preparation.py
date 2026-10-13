from types import SimpleNamespace
from unittest.mock import Mock

from module.map.assets import FLEET_1_ADVICE
from module.map.map_fleet_preparation import FleetOperator


def make_fleet(satisfied):
    """
    Args:
        satisfied (list): What is_hard_satisfied() answers on each screenshot.
    """
    main = SimpleNamespace(loop=lambda: iter(range(len(satisfied))), device=SimpleNamespace(click=Mock()))
    fleet = FleetOperator.__new__(FleetOperator)
    fleet.main = main
    fleet._advice = FLEET_1_ADVICE
    fleet._choose = 'FLEET_1_CHOOSE'
    fleet.is_hard_satisfied = Mock(side_effect=satisfied)
    return fleet


def test_advise_fills_a_hard_fleet_that_has_no_ships():
    fleet = make_fleet([False, True])

    assert fleet.advise() is True

    fleet.main.device.click.assert_called_once_with(FLEET_1_ADVICE)


def test_advise_leaves_a_prepared_hard_fleet_alone():
    fleet = make_fleet([True])

    assert fleet.advise() is True

    fleet.main.device.click.assert_not_called()


def test_advise_does_nothing_outside_hard_mode():
    fleet = make_fleet([None])

    assert fleet.advise() is None

    fleet.main.device.click.assert_not_called()
