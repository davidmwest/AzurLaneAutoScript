from datetime import datetime, timedelta
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

import alas
from alas import AzurLaneAutoScript
from module.handler.logged_out import logged_out_text


@pytest.mark.parametrize('text', [
    'Your account has logged in on another device. Please log in again.',
    'This account is logged in elsewhere',
    'Login information has expired, please re-login',
])
def test_popups_that_ask_to_log_in_again(text):
    assert logged_out_text(text)


@pytest.mark.parametrize('text', [
    'Login bonus, day 7',
    'Connection lost, retry?',
    'Retire the selected ships?',
    '',
])
def test_other_popups(text):
    assert not logged_out_text(text)


def scheduler(wait_minutes):
    script = AzurLaneAutoScript.__new__(AzurLaneAutoScript)
    script.config_name = 'test'
    script.__dict__['config'] = SimpleNamespace(Error_LoggedOutWait=wait_minutes, task_call=Mock())
    script.__dict__['device'] = SimpleNamespace(app_stop=Mock())
    return script


def test_logged_out_closes_the_game_and_logs_in_again_later():
    script = scheduler(60)

    script.handle_logged_out()

    script.device.app_stop.assert_called_once_with()
    script.config.task_call.assert_called_once_with('Restart')
    assert timedelta(minutes=59) < script.logged_out_until - datetime.now() <= timedelta(minutes=60)


def test_scheduler_holds_until_the_time_to_log_in_again(monkeypatch):
    script = scheduler(60)
    monkeypatch.setattr(alas, 'write_scheduler_state', Mock())
    monkeypatch.setattr(alas.time, 'sleep', lambda seconds: None)

    script.logged_out_until = datetime.now() + timedelta(seconds=0.2)
    assert script.wait_while_logged_out()
    assert script.logged_out_until is None
    # Nothing to wait for
    assert not script.wait_while_logged_out()


def test_no_check_when_the_wait_is_off():
    script = scheduler(0)

    assert not script.logged_out_on_screen()


def test_login_page_before_logging_in_is_not_a_log_out():
    """
    Like at the start of Alas, or after an update of the game: the game waits at its login page.
    """
    script = scheduler(60)
    script.device.logged_in = False
    script.device.screenshot = Mock()

    assert not script.logged_out_on_screen()
    script.device.screenshot.assert_not_called()
