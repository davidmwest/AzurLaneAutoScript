from datetime import datetime, timedelta
from types import SimpleNamespace
from unittest.mock import Mock, call

import pytest

import alas
from alas import AzurLaneAutoScript


class Config:
    def __init__(self, paused_checks):
        """
        Args:
            paused_checks (int): How many times the pause file is found before it is gone.
        """
        self.paused_checks = paused_checks

    @property
    def pause_requested(self):
        self.paused_checks -= 1
        return self.paused_checks >= 0


def make_scheduler(paused_checks):
    return SimpleNamespace(config=Config(paused_checks), config_name='alas', stop_event=None)


def test_a_task_that_keeps_failing_is_put_off_longer_each_time():
    delays, previous = [], None
    for _ in range(6):
        previous = alas.failed_task_delay(previous)
        delays.append(previous)

    assert delays == [20, 40, 80, 160, 240, 240]


def test_failed_task_is_put_off_and_counted_from_zero_again(monkeypatch):
    monkeypatch.setattr(alas, 'handle_notify', Mock())
    monkeypatch.setattr(alas, 'del_cached_property', Mock())
    config = SimpleNamespace(Error_OnePushConfig='provider: null', task_delay=Mock())
    scheduler = SimpleNamespace(config=config, config_name='alas', failure_record={'Event2': 3},
                                failure_delay={})

    assert AzurLaneAutoScript.put_off_failed_task(scheduler, 'Event2') == 20
    assert scheduler.failure_record == {'Event2': 0}
    config.task_delay.assert_called_once_with(minute=20, task='Event2')

    # Failing 3 times again without a success in between
    assert AzurLaneAutoScript.put_off_failed_task(scheduler, 'Event2') == 40
    # Another task starts from the beginning
    assert AzurLaneAutoScript.put_off_failed_task(scheduler, 'Event') == 20


class Runner(SimpleNamespace):
    """
    A scheduler whose task named `event2` raises the given error.
    """

    def __init__(self, keep_running, error):
        def task():
            raise error

        super().__init__(
            config=SimpleNamespace(Error_KeepRunning=keep_running, Error_OnePushConfig='provider: null',
                                   task_call=Mock()),
            config_name='alas',
            device=SimpleNamespace(screenshot=Mock(), sleep=Mock(), package='com.YoStarEN.AzurLane'),
            save_error_log=Mock(),
            # The game is not at its login page
            logged_out_on_screen=Mock(return_value=False),
            handle_logged_out=Mock(),
            event2=task,
        )


def test_unexpected_error_restarts_the_game_when_keep_running(monkeypatch):
    runner = Runner(keep_running=True, error=ValueError('something unexpected'))

    assert AzurLaneAutoScript.run(runner, 'event2') is False

    runner.config.task_call.assert_called_once_with('Restart')
    runner.save_error_log.assert_called_once_with()


def test_unexpected_error_ends_alas_without_keep_running(monkeypatch):
    monkeypatch.setattr(alas, 'handle_notify', Mock())
    runner = Runner(keep_running=False, error=ValueError('something unexpected'))

    with pytest.raises(SystemExit):
        AzurLaneAutoScript.run(runner, 'event2')

    runner.config.task_call.assert_not_called()


def test_scheduler_does_not_wait_without_a_pause(monkeypatch):
    sleep = Mock()
    monkeypatch.setattr(alas.time, 'sleep', sleep)
    write_state = Mock()
    monkeypatch.setattr(alas, 'write_scheduler_state', write_state)

    assert AzurLaneAutoScript.wait_while_paused(make_scheduler(paused_checks=0)) is False

    sleep.assert_not_called()
    write_state.assert_not_called()


def test_scheduler_waits_until_the_pause_is_over(monkeypatch):
    sleep = Mock()
    monkeypatch.setattr(alas.time, 'sleep', sleep)
    write_state = Mock()
    monkeypatch.setattr(alas, 'write_scheduler_state', write_state)

    # Found at the first look, and on 3 more looks while waiting
    assert AzurLaneAutoScript.wait_while_paused(make_scheduler(paused_checks=4)) is True

    assert sleep.call_count == 3
    # Tells the GUI it holds, then that it goes on
    assert write_state.call_args_list == [call('alas', paused=True), call('alas')]


def test_waiting_for_the_next_task_ends_for_a_pause(monkeypatch):
    sleep = Mock()
    monkeypatch.setattr(alas.time, 'sleep', sleep)
    config = SimpleNamespace(start_watching=Mock(), should_reload=lambda: False, pause_requested=True)
    scheduler = SimpleNamespace(config=config, config_name='alas', stop_event=None)

    # Not after 3 hours of waiting for oil
    assert AzurLaneAutoScript.wait_until(scheduler, datetime.now() + timedelta(hours=3)) is False
    assert sleep.call_count == 1


def test_next_task_holds_while_paused_first(monkeypatch):
    import module.base.resource
    monkeypatch.setattr(module.base.resource, 'release_resources', Mock())
    calls = []
    task = SimpleNamespace(command='Event2', next_run=datetime.now() - timedelta(minutes=1))

    def get_next():
        calls.append('get_next')
        return task

    config = SimpleNamespace(get_next=get_next, bind=Mock(), task=None)
    scheduler = SimpleNamespace(config=config, wait_while_paused=lambda: calls.append('hold'),
                                wait_while_logged_out=lambda: calls.append('logged out'))

    assert AzurLaneAutoScript.get_next_task(scheduler) == 'Event2'
    assert calls == ['hold', 'logged out', 'get_next']


def test_logged_out_during_a_task_waits_instead_of_restarting_at_once():
    from module.exception import GameLoggedOutError
    runner = Runner(keep_running=True, error=GameLoggedOutError('Login page during a task'))

    assert AzurLaneAutoScript.run(runner, 'event2') is False

    runner.handle_logged_out.assert_called_once_with()
    runner.config.task_call.assert_not_called()


def test_stuck_at_the_login_page_waits_too():
    from module.exception import GameStuckError
    runner = Runner(keep_running=True, error=GameStuckError('Wait too long'))
    runner.logged_out_on_screen = Mock(return_value=True)

    assert AzurLaneAutoScript.run(runner, 'event2') is False

    runner.handle_logged_out.assert_called_once_with()
    runner.config.task_call.assert_not_called()
