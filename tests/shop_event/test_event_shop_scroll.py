"""
The scroll of the event shop is translucent, and part of it lies over dark character art
where the button can hardly be told from the background.

Files in ./data are cut from screenshots of the EN client: the scroll area with 3 pixels of page on each side.
The scroll is 422 rows, the button 119. Files named scroll_at_<row>.png have the button starting at that row,
known from how far the items had moved.
"""
import os
from types import SimpleNamespace

import cv2
import numpy as np
import pytest

from module.shop_event.ui import EVENT_SHOP_SCROLL

DATA = os.path.join(os.path.dirname(__file__), 'data')
SCROLL_COLOR = np.array(EVENT_SHOP_SCROLL.color, dtype=np.float32)


@pytest.fixture(autouse=True)
def scroll():
    """
    A scroll that has not seen any shop yet.
    """
    EVENT_SHOP_SCROLL.button_length = None
    yield EVENT_SHOP_SCROLL
    EVENT_SHOP_SCROLL.button_length = None


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


def test_scroll_at_top(scroll):
    main = load('scroll_top.png')

    assert runs(scroll.match_color(main)) == [(0, 119)]
    assert scroll.cal_position(main) == 0.0
    assert scroll.at_top(main)
    assert not scroll.at_bottom(main)


def test_scroll_at_bottom(scroll):
    main = load('scroll_bottom.png')

    assert runs(scroll.match_color(main)) == [(302, 421)]
    assert scroll.at_bottom(main)
    assert not scroll.at_top(main)


def test_button_length_is_measured_at_the_top(scroll):
    scroll.match_color(load('scroll_at_164.png'))
    assert scroll.button_length is None

    scroll.match_color(load('scroll_top.png'))
    assert scroll.button_length == 119

    # and kept away from the top
    scroll.match_color(load('scroll_at_164.png'))
    assert scroll.button_length == 119


@pytest.mark.parametrize('start, tolerance', [
    (31, 2),
    (80, 2),
    (164, 2),
    (214, 2),
    (249, 4),
    (292, 2),
    # All of the button lies on the dark part of the page here, it could be anywhere within some 30 rows
    (241, 20),
    (273, 20),
])
def test_scroll_between_top_and_bottom(scroll, start, tolerance):
    scroll.match_color(load('scroll_top.png'))
    main = load(f'scroll_at_{start:03d}.png')

    (found, end), = runs(scroll.match_color(main))

    assert abs(found - start) <= tolerance
    assert end - found == 119
    assert scroll.cal_position(main) == pytest.approx(start / (422 - 119), abs=tolerance / (422 - 119))


def test_button_of_unknown_length_is_still_one_piece(scroll):
    # Without the length, the end on the dark part of the page is a guess
    (found, end), = runs(scroll.match_color(load('scroll_at_080.png')))

    assert abs(found - 80) <= 2
    assert end - found > 119


def test_no_button_is_seen_where_there_is_no_scroll(scroll):
    scroll.match_color(load('scroll_top.png'))
    page = np.full((422, 7, 3), 200, dtype=np.uint8)

    assert not scroll.match_color(page_with(page)).any()


@pytest.mark.parametrize('button', [(0, 30), (10, 40)])
def test_button_is_one_piece_even_if_rows_elsewhere_look_like_it(scroll, button):
    total = scroll.area[3] - scroll.area[1]
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

    mask = scroll.match_color(page_with(page))

    assert runs(mask) == [button]
