"""Tests for CounterOcr.after_process in module.shop_event.item."""
import os

import cv2
import numpy as np
import pytest

from module.config import server
from module.ocr.ocr import Ocr
from module.shop_event import item
from module.shop_event.item import CounterOcr, EventShopItem

AMBIGUOUS_SLASHLESS_COUNTERS = {'15', '015', '350', '0350', '1350', '2350', '3350', '4350'}


class TestCounterOcrAfterProcess:
    """Test the pure string post-processing of CounterOcr.after_process.

    after_process only rewrites the OCR result string (letter-to-digit
    revisions and the "55" -> "5/5" counter fixup), so the test calls the
    method directly on a CounterOcr instance without any image or OCR model
    involved.
    """

    ocr = CounterOcr([], name='Test_counter_ocr')

    @pytest.mark.parametrize('raw, expected', [
        # No revision needed
        ('14/15', '14/15'),
        ('0/1', '0/1'),
        ('0123456789/0123456789', '0123456789/0123456789'),
        ('', ''),
        # Single letter revision
        ('D', '0'),
        ('B', '8'),
        ('I', '1'),
        ('S', '5'),
        # Letters mixed with digits and each other
        ('I4/IS', '14/15'),
        ('DB/SB', '08/58'),
        ('IBS/DD', '185/00'),
        ('ISB', '158'),
        ('DS', '0/5'),
        ('I/D/S/B', '1/0/5/8'),
        ('IIDDSSBB', '11005588'),
        ('2B/2B', '28/28'),
        ('3I/D9', '31/09'),
    ])
    def test_letter_revision(self, raw, expected):
        """Letters are revised to digits, then the counter fixup applies."""
        assert self.ocr.after_process(raw) == expected

    @pytest.mark.parametrize('raw, expected', [
        ('55', '5/5'),
        ('2530', '25/30'),
        ('1515', '15/15'),
        ('350350', '350/350'),
        ('500500', '500/500'),
    ])
    def test_fixup_documented_examples(self, raw, expected):
        """Documented examples in the fixup comment."""
        assert self.ocr.after_process(raw) == expected

    @pytest.mark.parametrize('raw, expected', [
        # "0100" -> "0/100", ..., "100100" -> "100/100", and likewise for
        # every other total in the fixup list
        (f'{current}{total}', f'{current}/{total}')
        for total in [500, 350, 100, 50, 40, 30, 20, 15, 10, 5, 4, 2, 1]
        for current in range(0, total + 1)
        if f'{current}{total}' not in AMBIGUOUS_SLASHLESS_COUNTERS
    ])
    def test_fixup_range(self, raw, expected):
        """Every unambiguous current in 0..total gets the slash inserted correctly."""
        assert self.ocr.after_process(raw) == expected

    @pytest.mark.parametrize('raw, expected', [
        # Edge case: OCR result is exactly the total, no slash is added
        ('500', '500'),
        ('350', '350'),
        ('100', '100'),
        ('50', '50'),
        ('30', '30'),
        ('40', '40'),
        ('20', '20'),
        ('15', '15'),
        ('10', '10'),
        ('5', '5'),
        ('4', '4'),
        ('2', '2'),
        ('1', '1'),
    ])
    def test_fixup_exact_total_unchanged(self, raw, expected):
        assert self.ocr.after_process(raw) == expected

    @pytest.mark.parametrize('raw', sorted(AMBIGUOUS_SLASHLESS_COUNTERS))
    def test_fixup_ambiguous_counter_unchanged(self, raw):
        assert self.ocr.after_process(raw) == raw

    @pytest.mark.parametrize('raw, expected', [
        # Pure digits that do not end with any total stay unchanged
        ('77', '77'),
        ('233', '233'),
        ('68', '68'),
        ('93', '93'),
        ('813', '813'),
    ])
    def test_fixup_no_total_match(self, raw, expected):
        assert self.ocr.after_process(raw) == expected

    @pytest.mark.parametrize('raw, expected', [
        ('0/500', [0, 500]),
        ('500/500', [500, 500]),
        ('15/15', [15, 15]),
        ('14/15', [14, 15]),
    ])
    def test_parse_valid_counter(self, raw, expected):
        assert self.ocr.parse_result(raw) == expected

    @pytest.mark.parametrize('raw', [
        '', '/', '/500', '500/', '500', '500/50', '0/0', '1/2/3',
    ])
    def test_parse_invalid_counter(self, raw):
        assert self.ocr.parse_result(raw) == [0, 0]

    def test_ocr_invalid_counter_returns_sentinel(self, monkeypatch):
        monkeypatch.setattr(Ocr, 'ocr', lambda *args, **kwargs: ['/', '500/500'])
        blank = np.full((16, 60, 3), 255, dtype=np.uint8)

        assert self.ocr.ocr([blank, blank], direct_ocr=True) == [[0, 0], [500, 500]]


@pytest.mark.parametrize('readings, expected', [
    # The reading most agree on
    (['10/0', '10/10', '10/10'], '10/10'),
    (['100/100', '00/100', '100/100'], '100/100'),
    # Readings that are not a counter have no vote
    (['10/0', '500/50', '10/10'], '10/10'),
    (['1/1', '1/1', '/1'], '1/1'),
    # The earlier reading on a tie
    (['4/10', '4/1', ''], '4/10'),
    # Nothing to choose from
    (['10/0', '', '/'], '10/0'),
])
def test_counter_vote(readings, expected):
    assert CounterOcr.vote(readings) == expected


@pytest.mark.parametrize('readings, glyphs, expected', [
    # Most readings lost a letter, the picture has 7
    (['00/100', '00/100', '100/100'], 7, '100/100'),
    (['0/10', '0/10', '10/10', '0/10'], 5, '10/10'),
    # Letters that touch can not be counted, back to what most agree on
    (['4/4', '4/4', '4/4'], 2, '4/4'),
    (['4/10', '4/1', '4/10'], 2, '4/10'),
    # A reading that is not a counter does not win by its length
    (['10/0', '10/10', '4/1'], 4, '10/10'),
])
def test_counter_vote_prefers_readings_as_long_as_the_picture(readings, glyphs, expected):
    assert CounterOcr.vote(readings, glyphs) == expected


@pytest.mark.parametrize('columns, expected', [
    ('', 0),
    ('    ', 0),
    ('## ', 1),
    (' # ## #', 3),
    ('#######', 1),
])
def test_count_glyphs(columns, expected):
    image = np.full((16, len(columns)), 255, dtype=np.uint8)
    for x, column in enumerate(columns):
        if column == '#':
            image[4:12, x] = 0

    assert CounterOcr.count_glyphs(image) == expected


def load_counters(name):
    """
    Files in ./data are the "Limit:10/10" lines of items on screenshots of the EN client, one above the other.
    """
    image = cv2.cvtColor(cv2.imread(os.path.join(os.path.dirname(__file__), 'data', name)), cv2.COLOR_BGR2RGB)
    return [image[y:y + 16] for y in range(0, image.shape[0], 16)]


@pytest.mark.parametrize('name, expected', [
    # "10/10" of the 8th item came back as "10/0" at the usual letter threshold
    ('counters.png', [
        [10, 10], [1, 1], [1, 1], [350, 350], [500, 500],
        [1, 1], [5, 5], [10, 10], [4, 10], [5, 5],
    ]),
    # "10/10" of the 6th item came back as "0/10" at any letter threshold,
    # and "100/100" of the last two as "00/100" and "100/00" in most ways of reading
    ('counters_2.png', [
        [1, 1], [350, 350], [495, 500], [5, 5], [10, 10],
        [10, 10], [5, 5], [2, 2], [30, 30], [10, 10],
        [100, 100], [100, 100],
    ]),
])
def test_reads_the_stock_counters_of_a_shop_screen(monkeypatch, name, expected):
    monkeypatch.setattr(server, 'server', 'en')
    ocr = CounterOcr([], letter=item.COUNTER_COLOR, name='Test_counter_ocr')

    assert ocr.ocr(load_counters(name), direct_ocr=True) == expected
    assert (ocr.margin, ocr.threshold) == (0, 128)


def test_price_135_total_15_is_equip_ssr():
    item = object.__new__(EventShopItem)
    item.price = 135
    item.total_count = 15
    item.name = 'Unknown'

    item.correct_name_and_cost()

    assert item.name == 'EquipSSR'
    assert item.cost == 'pt'
