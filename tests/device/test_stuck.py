from types import SimpleNamespace
from unittest.mock import Mock

import numpy as np
import pytest

from module.device import device as device_module
from module.device.device import Device
from module.exception import GameStuckError


class Clock:
    def __init__(self):
        self.now = 1000.

    def time(self):
        return self.now


@pytest.fixture
def clock(monkeypatch):
    clock = Clock()
    monkeypatch.setattr(device_module, 'time', clock)
    return clock


def make_device(waiting_for, waited=70, waited_long=False):
    """
    Args:
        waiting_for (set[str]): Buttons looked for since the last thing that was handled.
        waited (int): Seconds since then.
        waited_long (bool): If that is longer than even a battle may take.
    """
    device = SimpleNamespace(
        image=np.zeros((720, 1280, 3), dtype=np.uint8),
        detect_record=set(waiting_for),
        stuck_timer=SimpleNamespace(reached=lambda: waited > 60),
        stuck_timer_long=SimpleNamespace(reached=lambda: waited_long),
        stuck_long_wait_list=Device.stuck_long_wait_list,
        stuck_frozen_wait_list=Device.stuck_frozen_wait_list,
        stuck_frozen_seconds=Device.stuck_frozen_seconds,
        _frozen_sample=None,
        _frozen_since=0.,
        stuck_record_clear=Mock(),
        app_is_running=Mock(return_value=True),
    )
    device.is_screen_frozen = lambda: Device.is_screen_frozen(device)
    return device


def show(device, clock, seconds, changed):
    """
    Take screenshots for some seconds, of a screen that changes or does not.
    """
    for _ in range(seconds):
        clock.now += 1
        if changed:
            device.image = device.image.copy()
            device.image[100:200, 100:200] += 1
        Device.frozen_record_update(device)


def test_screen_is_frozen_after_not_changing_for_a_while(clock):
    device = make_device({'PAUSE'})

    show(device, clock, seconds=20, changed=False)
    assert Device.is_screen_frozen(device) is False

    show(device, clock, seconds=20, changed=False)
    assert Device.is_screen_frozen(device) is True

    show(device, clock, seconds=1, changed=True)
    assert Device.is_screen_frozen(device) is False


def test_battle_that_stands_still_is_stuck_without_the_long_wait(clock):
    device = make_device({'PAUSE', 'COMBAT_AUTO'})
    show(device, clock, seconds=40, changed=False)

    with pytest.raises(GameStuckError):
        Device.stuck_record_check(device)


def test_battle_that_goes_on_gets_the_long_wait(clock):
    device = make_device({'PAUSE', 'COMBAT_AUTO'})
    show(device, clock, seconds=40, changed=True)

    assert Device.stuck_record_check(device) is False


def test_login_may_stand_still(clock):
    # Checking for updates and connecting show the same picture for a long time
    device = make_device({'LOGIN_CHECK'})
    show(device, clock, seconds=40, changed=False)

    assert Device.stuck_record_check(device) is False


def test_long_wait_still_ends(clock):
    device = make_device({'PAUSE'}, waited=200, waited_long=True)
    show(device, clock, seconds=5, changed=True)

    with pytest.raises(GameStuckError):
        Device.stuck_record_check(device)
