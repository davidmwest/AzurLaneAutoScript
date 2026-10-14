from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from module.retire.scheduled import RetireShips


class Config(SimpleNamespace):
    def override(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


def retire_ships(mode, retired=10):
    task = RetireShips.__new__(RetireShips)
    task.config = Config(Retirement_RetireMode=mode, task_delay=Mock())
    for method in ['ui_ensure', 'retire_page_enter', 'handle_dock_cards_loading', '_retirement_quit']:
        setattr(task, method, Mock())
    task.retire_ships_one_click = Mock(return_value=retired)
    task.retire_ships_old = Mock(return_value=retired)
    return task


@pytest.mark.parametrize('mode', ['one_click_retire', 'enhance'])
def test_retire_ships_with_the_quick_retire_options_of_the_game(mode):
    task = retire_ships(mode)

    task.run()

    task.retire_ships_one_click.assert_called_once_with()
    task.retire_ships_old.assert_not_called()
    # The game asks to confirm rare ships as with one_click_retire
    assert task.config.Retirement_RetireMode == 'one_click_retire'
    task.config.task_delay.assert_called_once_with(server_update=True)


def test_retire_ships_with_the_old_retire_options():
    task = retire_ships('old_retire')

    task.run()

    task.retire_ships_old.assert_called_once_with()
    task.retire_ships_one_click.assert_not_called()


def test_nothing_to_retire_is_fine():
    task = retire_ships('one_click_retire', retired=0)

    task.run()

    task._retirement_quit.assert_called_once_with()
    task.config.task_delay.assert_called_once_with(server_update=True)


def test_do_not_retire_does_not_even_open_the_page():
    task = retire_ships('do_not_retire')

    task.run()

    task.ui_ensure.assert_not_called()
    task.retire_ships_one_click.assert_not_called()
    task.config.task_delay.assert_called_once_with(server_update=True)
