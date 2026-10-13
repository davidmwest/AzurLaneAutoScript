from types import SimpleNamespace
from unittest.mock import Mock

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


def test_scheduler_does_not_wait_without_a_pause(monkeypatch):
    sleep = Mock()
    monkeypatch.setattr(alas.time, 'sleep', sleep)

    assert AzurLaneAutoScript.wait_while_paused(make_scheduler(paused_checks=0)) is False

    sleep.assert_not_called()


def test_scheduler_waits_until_the_pause_is_over(monkeypatch):
    sleep = Mock()
    monkeypatch.setattr(alas.time, 'sleep', sleep)

    # Found at the first look, and on 3 more looks while waiting
    assert AzurLaneAutoScript.wait_while_paused(make_scheduler(paused_checks=4)) is True

    assert sleep.call_count == 3
