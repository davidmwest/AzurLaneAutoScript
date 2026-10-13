from types import SimpleNamespace
from unittest.mock import Mock

from module.base.timer import Timer
from module.handler.assets import GAME_TIPS, GAME_TIPS3
from module.handler.info_handler import InfoHandler


def make_handler(looks_like_game_tips):
    """
    Args:
        looks_like_game_tips (list[bool]): What each screenshot looks like.
    """
    screenshots = iter(looks_like_game_tips)
    return SimpleNamespace(
        device=SimpleNamespace(click=Mock()),
        is_game_tips=lambda: next(screenshots),
        # No waiting in tests, game tips are closed once they have been seen often enough
        _game_tips_seen=Timer(-1, count=2),
    )


def test_game_tips_that_stay_are_closed():
    handler = make_handler([True, True, True, True])

    handled = [InfoHandler.handle_game_tips(handler) for _ in range(4)]

    assert handled == [False, False, False, True]
    handler.device.click.assert_called_once_with(GAME_TIPS)


def test_a_screen_that_looks_like_game_tips_for_a_moment_is_left_alone():
    # The details of a ship sliding in, the button to close game tips is where UNLOCK of the ship is
    handler = make_handler([True, True, False, True, True, True, False])

    handled = [InfoHandler.handle_game_tips(handler) for _ in range(7)]

    assert not any(handled)
    handler.device.click.assert_not_called()


def test_game_tips_are_told_by_page_number_and_dark_button():
    handler = SimpleNamespace(
        appear=Mock(side_effect=lambda button, **kwargs: button is GAME_TIPS3),
        image_color_count=Mock(return_value=True),
    )
    assert InfoHandler.is_game_tips(handler) is True

    handler.image_color_count = Mock(return_value=False)
    assert InfoHandler.is_game_tips(handler) is False

    handler.appear = Mock(return_value=False)
    assert InfoHandler.is_game_tips(handler) is False
