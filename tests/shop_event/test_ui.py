import os
from datetime import datetime
from types import SimpleNamespace
from unittest.mock import Mock

import cv2
import numpy as np
import pytest

from module.shop.assets import SHOP_OCR_BALANCE
from module.shop_event.assets import SHOP_OCR_BALANCE_SECOND
from module.shop_event.ui import EVENT_SHOP_TAB_AREA, EventShopUI, parse_event_shop_deadline

DATA = os.path.join(os.path.dirname(__file__), 'data')


class Shop:
    """
    An event shop that shows the given screenshots one after another.
    """
    event_shop_tab_count = EventShopUI.event_shop_tab_count

    def __init__(self, frames):
        self.frames = frames
        self.shown = 0
        self.device = SimpleNamespace(image=None)

    def loop(self, timeout=None):
        for frame in self.frames:
            self.device.image = frame
            self.shown += 1
            yield frame


def screenshot(tab_bar_shown=1.0):
    """
    Args:
        tab_bar_shown (float): How much of the tab bar has appeared, from the left.
    """
    x1, y1, x2, y2 = EVENT_SHOP_TAB_AREA
    tab_bar = cv2.cvtColor(cv2.imread(os.path.join(DATA, 'tab_bar_one_tab.png')), cv2.COLOR_BGR2RGB)
    tab_bar[:, int(tab_bar.shape[1] * tab_bar_shown):] = 0
    image = np.zeros((720, 1280, 3), dtype=np.uint8)
    image[y1:y2, x1:x2] = tab_bar
    return image


def shop_with_balances(swap_icons=False):
    """
    ./data/balances.png is the area (800, 150, 1070, 200) of an event shop
    with the event points on the left and the UR vouchers on the right.
    """
    balances = cv2.cvtColor(cv2.imread(os.path.join(DATA, 'balances.png')), cv2.COLOR_BGR2RGB)
    image = np.zeros((720, 1280, 3), dtype=np.uint8)
    image[150:200, 800:1070] = balances
    if swap_icons:
        left, right = (816, 845), (943, 972)
        image[150:200, left[0]:left[1]], image[150:200, right[0]:right[1]] = \
            image[150:200, right[0]:right[1]].copy(), image[150:200, left[0]:left[1]].copy()
    shop = SimpleNamespace(image_crop=lambda area, copy=True: image[area[1]:area[3], area[0]:area[2]])
    shop.is_ur_voucher_balance = lambda button: EventShopUI.is_ur_voucher_balance(shop, button)
    shop.ui_process_check_button = Mock(return_value=False)
    return shop


def test_event_points_left_of_the_ur_vouchers():
    shop = shop_with_balances()

    assert EventShopUI.is_ur_voucher_balance(shop, SHOP_OCR_BALANCE) is True
    assert EventShopUI.is_ur_voucher_balance(shop, SHOP_OCR_BALANCE_SECOND) is False
    assert EventShopUI.is_pt_reversed.func(shop) is True
    shop.ui_process_check_button.assert_not_called()


def test_event_points_right_of_the_ur_vouchers():
    shop = shop_with_balances(swap_icons=True)

    assert EventShopUI.is_pt_reversed.func(shop) is False
    shop.ui_process_check_button.assert_not_called()


def test_known_events_decide_where_the_event_points_are_if_the_icons_do_not():
    shop = shop_with_balances()
    shop.is_ur_voucher_balance = lambda button: False
    shop.ui_process_check_button = Mock(return_value=True)

    assert EventShopUI.is_pt_reversed.func(shop) is True


@pytest.mark.parametrize('period, today, expected', [
    (':2026.8.13~2026.9.3', datetime(2026, 8, 20), datetime(2026, 9, 4)),
    (':2026.12.25~2027.1.8', datetime(2026, 12, 28), datetime(2027, 1, 9)),
    # EN, no years
    (':10.8-10.21', datetime(2026, 10, 13), datetime(2026, 10, 22)),
    (':10.8-10.21', datetime(2026, 10, 21, 23), datetime(2026, 10, 22)),
    (':12.25-1.8', datetime(2026, 12, 28), datetime(2027, 1, 9)),
    (':12.25-1.8', datetime(2027, 1, 2), datetime(2027, 1, 9)),
    # Not a period
    ('', datetime(2026, 10, 13), None),
    (':10.8', datetime(2026, 10, 13), None),
    (':10.8-13.45', datetime(2026, 10, 13), None),
])
def test_parse_event_shop_deadline(period, today, expected):
    assert parse_event_shop_deadline(period, today) == expected


def test_one_tab():
    shop = Shop([screenshot(), screenshot()])

    count, navbar = EventShopUI.event_shop_tab_count_and_navbar.func(shop)

    assert count == 1
    assert tuple(navbar.grids.grid_shape) == (1, 1)


def test_tab_count_waits_for_the_tab_bar_to_appear():
    shop = Shop([screenshot(tab_bar_shown=0.3), screenshot(), screenshot(), screenshot()])

    count, navbar = EventShopUI.event_shop_tab_count_and_navbar.func(shop)

    assert count == 1
    assert shop.shown == 3
