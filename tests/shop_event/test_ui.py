import os
from types import SimpleNamespace

import cv2
import numpy as np

from module.shop_event.ui import EVENT_SHOP_TAB_AREA, EventShopUI

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
