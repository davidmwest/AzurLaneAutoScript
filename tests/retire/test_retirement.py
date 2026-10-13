from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from module.exception import RequestHumanTakeover
from module.retire.assets import RETIRE_APPEAR_1
from module.retire.retirement import Retirement


def make_retirement(mode, dock_full):
    return SimpleNamespace(
        config=SimpleNamespace(Retirement_RetireMode=mode),
        handle_game_tips=Mock(return_value=False),
        appear=Mock(side_effect=lambda button, **kwargs: dock_full and button is RETIRE_APPEAR_1),
        appear_then_click=Mock(return_value=False),
        _unable_to_enhance=False,
        _retire_handler=Mock(),
        _enhance_handler=Mock(),
    )


def test_do_not_retire_stops_when_the_dock_is_full():
    retirement = make_retirement('do_not_retire', dock_full=True)

    with pytest.raises(RequestHumanTakeover):
        Retirement.handle_retirement(retirement)

    retirement.appear_then_click.assert_not_called()
    retirement._retire_handler.assert_not_called()
    retirement._enhance_handler.assert_not_called()


def test_do_not_retire_leaves_other_screens_alone():
    retirement = make_retirement('do_not_retire', dock_full=False)

    assert Retirement.handle_retirement(retirement) is False

    retirement.appear_then_click.assert_not_called()
    retirement._retire_handler.assert_not_called()


def test_one_click_retire_still_opens_retirement_when_the_dock_is_full():
    retirement = make_retirement('one_click_retire', dock_full=True)
    retirement.appear_then_click = Mock(side_effect=lambda button, **kwargs: button is RETIRE_APPEAR_1)
    retirement.interval_clear = Mock()
    retirement.interval_reset = Mock()
    retirement.map_cat_attack_timer = Mock()

    assert Retirement.handle_retirement(retirement) is False

    assert retirement.appear_then_click.call_args[0][0] is RETIRE_APPEAR_1
