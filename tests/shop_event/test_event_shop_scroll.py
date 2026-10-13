"""
The scroll of the event shop is translucent, and part of it lies over dark character art
where the button can hardly be told from the background.

Files in ./data are cut from screenshots of the EN client: the scroll area with 3 pixels of page on each side.
"""
import os
from types import SimpleNamespace

import cv2
import numpy as np
import pytest

from module.shop_event.ui import EVENT_SHOP_SCROLL

DATA = os.path.join(os.path.dirname(__file__), 'data')
SCROLL_COLOR = np.array(EVENT_SHOP_SCROLL.color, dtype=np.float32)


def page_with(image):
    return SimpleNamespace(image_crop=lambda area, copy=True: image)


def load(name):
    return page_with(cv2.cvtColor(cv2.imread(os.path.join(DATA, name)), cv2.COLOR_BGR2RGB))


def runs(mask):
    """
    Returns:
        list[tuple[int, int]]: Start and end of each stretch of True, end not included.
    """
    edges = np.flatnonzero(np.diff(np.concatenate(([0], mask.astype(int), [0]))))
    return list(zip(edges[::2].tolist(), edges[1::2].tolist()))


def test_scroll_at_top():
    main = load('scroll_top.png')

    assert runs(EVENT_SHOP_SCROLL.match_color(main)) == [(0, 119)]
    assert EVENT_SHOP_SCROLL.cal_position(main) == 0.0
    assert EVENT_SHOP_SCROLL.at_top(main)
    assert not EVENT_SHOP_SCROLL.at_bottom(main)


def test_scroll_in_the_middle():
    main = load('scroll_middle.png')

    assert len(runs(EVENT_SHOP_SCROLL.match_color(main))) == 1
    assert 0.4 < EVENT_SHOP_SCROLL.cal_position(main) < 0.6


def test_scroll_at_bottom():
    main = load('scroll_bottom.png')

    assert runs(EVENT_SHOP_SCROLL.match_color(main)) == [(302, 421)]
    assert EVENT_SHOP_SCROLL.at_bottom(main)
    assert not EVENT_SHOP_SCROLL.at_top(main)


@pytest.mark.parametrize('button', [(0, 30), (10, 40)])
def test_button_is_one_piece_even_if_rows_elsewhere_look_like_it(button):
    total = EVENT_SHOP_SCROLL.area[3] - EVENT_SHOP_SCROLL.area[1]
    page = np.full((total, 7, 3), 200, dtype=np.float32)
    # The page is as dark as the scroll here, and not quite even
    page[60:] = SCROLL_COLOR + 2
    opacity = np.full((total, 1), 0.2, dtype=np.float32)
    opacity[button[0]:button[1]] = 0.5
    page[:, 3] = opacity * SCROLL_COLOR + (1 - opacity) * page[:, 3]
    page[60::2, 3] -= 3
    page[61::2, 3] += 3
    page = np.rint(page).astype(np.uint8)
    # Taken on their own, half of the dark rows are closer to the button than to the background
    centre, around = page[60:, 3].astype(int), page[60:, 0].astype(int)
    assert np.count_nonzero(np.all(centre < around, axis=1)) == (total - 60) // 2

    mask = EVENT_SHOP_SCROLL.match_color(page_with(page))

    assert runs(mask) == [button]
