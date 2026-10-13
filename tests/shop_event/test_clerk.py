from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from module.shop_event import clerk
from module.shop_event.clerk import EventShopClerk, ItemNotFoundError


def make_clerk(counter_results):
    scanner = SimpleNamespace(grids=None, items=[])
    results = iter(counter_results)

    def predict(*args, **kwargs):
        count, total_count = next(results)
        scanner.items = [SimpleNamespace(
            count=count,
            total_count=total_count,
            button=(0, 100, 1, 101),
        )]

    scanner.predict = Mock(side_effect=predict)
    scanner.extract_template = Mock()
    grid = Mock()
    grid.__getitem__ = Mock(return_value=SimpleNamespace(area=(0, 100, 1, 101)))
    clerk = SimpleNamespace(
        ensure_no_info_bar=Mock(),
        event_shop_items=scanner,
        _get_event_shop_grid=Mock(return_value=grid),
        config=SimpleNamespace(SHOP_EXTRACT_TEMPLATE=False),
        device=SimpleNamespace(image=object(), screenshot=Mock()),
    )
    return clerk, scanner


def make_item(name, y, count=1):
    return SimpleNamespace(name=name, price=100, count=count, total_count=5, button=(0, y, 1, y + 1))


def names(rows):
    return [[item.name for item in row] for row in rows]


def test_merge_first_screen_into_rows():
    screen = [make_item('a', 239), make_item('b', 239), make_item('c', 463)]

    assert names(EventShopClerk.merge_scanned_rows([], screen)) == [['a', 'b'], ['c']]


def test_merge_ignores_rows_already_scanned():
    rows = [[make_item('a', 239)], [make_item('b', 463)]]
    screen = [make_item('b', 300), make_item('c', 524)]

    assert names(EventShopClerk.merge_scanned_rows(rows, screen)) == [['a'], ['b'], ['c']]


def test_merge_same_screen_again_adds_nothing():
    rows = [[make_item('a', 239)], [make_item('b', 463)]]
    screen = [make_item('a', 239), make_item('b', 463)]

    assert names(EventShopClerk.merge_scanned_rows(rows, screen)) == [['a'], ['b']]


def test_merge_keeps_a_row_that_only_looks_alike():
    rows = [[make_item('a', 239, count=5)]]
    screen = [make_item('a', 239, count=3)]

    assert names(EventShopClerk.merge_scanned_rows(rows, screen)) == [['a'], ['a']]


def test_merge_rows_from_different_screens_at_the_same_height_stay_apart():
    rows = [[make_item('a', 300)], [make_item('b', 300)]]
    screen = [make_item('b', 300), make_item('c', 524)]

    assert names(EventShopClerk.merge_scanned_rows(rows, screen)) == [['a'], ['b'], ['c']]


class Shop:
    """
    An event shop that shows the given screens one after another while scrolling down.
    The scroll counts as at bottom one screen before the last.
    """

    def __init__(self, screens):
        self.screens = screens
        self.shown = 0
        self.dragged_to_end = 0
        self.button_length = 119
        self.device = SimpleNamespace(click_record_clear=Mock())
        self.merge_scanned_rows = EventShopClerk.merge_scanned_rows

    def event_shop_get_items(self, scroll_pos=None):
        return self.screens[self.shown]

    # Scroll
    def set_top(self, main):
        self.shown = 0

    def cal_position(self, main):
        return self.shown / (len(self.screens) - 1)

    def at_bottom(self, main):
        return self.shown >= len(self.screens) - 2

    def next_page(self, main, page):
        self.shown += 1

    def drag_to_end(self, main):
        self.shown = len(self.screens) - 1
        self.dragged_to_end += 1


def test_scan_all_reads_every_row_once(monkeypatch):
    shop = Shop([
        [make_item('a', 239), make_item('b', 463)],
        [make_item('b', 332)],
        [make_item('c', 425)],
        # The last row is only shown at the very end
        [make_item('c', 248), make_item('d', 471)],
    ])
    monkeypatch.setattr(clerk, 'EVENT_SHOP_SCROLL', shop)

    items = EventShopClerk.scan_all(shop)

    assert [item.name for item in items] == ['a', 'b', 'c', 'd']
    assert shop.dragged_to_end == 1
    # Another shop has another amount of items
    assert shop.button_length is None


def test_event_shop_get_items_does_not_reshoot_valid_scan():
    clerk, scanner = make_clerk([(1, 1)])

    EventShopClerk.event_shop_get_items(clerk)

    assert scanner.predict.call_count == 1
    clerk.device.screenshot.assert_not_called()


def test_event_shop_get_items_reshoots_invalid_counter():
    clerk, scanner = make_clerk([(0, 0), (1, 1)])

    items = EventShopClerk.event_shop_get_items(clerk)

    assert (items[0].count, items[0].total_count) == (1, 1)
    assert scanner.predict.call_count == 2
    clerk.device.screenshot.assert_called_once_with()


def test_event_shop_get_items_rejects_persistent_invalid_counter():
    clerk, scanner = make_clerk([(0, 0), (0, 0), (0, 0)])

    with pytest.raises(ItemNotFoundError):
        EventShopClerk.event_shop_get_items(clerk)

    assert scanner.predict.call_count == 3
    assert clerk.device.screenshot.call_count == 2
