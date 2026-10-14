import os
from datetime import datetime, timedelta

import cv2
import pytest

import module.config.server as server
from module.base.button import Button
from module.base.utils import crop
from module.map.lineup_rotation import SLOTS_PER_FLEET, lineup_slot
from module.mood.dorm_rest import PickerCard, DormShip, picker_fleets_ended, picker_is_top, picker_row_tops, \
    read_dorm_floor, read_picker_row, ship_list_tab, update_moods
from module.mood.lineup import level_area, match_lineup, portrait_area
from module.mood.ship import ShipMood, ShipMoods, portrait_signature
from module.ocr.ocr import Digit

DATA = os.path.join(os.path.dirname(__file__), 'data')
NOW = datetime(2026, 10, 14, 8, 0, 0)


@pytest.fixture(autouse=True)
def en():
    # Templates take the files of the server set when they are loaded, set_server() releases them
    previous = server.server
    server.set_server('en')
    yield
    server.set_server(previous)


def load(name):
    """
    Frames of the EN client at 2560x1440 as Alas sees them, black except the parts read.
    """
    return cv2.cvtColor(cv2.imread(os.path.join(DATA, name)), cv2.COLOR_BGR2RGB)


class Config:
    def cross_get(self, keys, default=None):
        return default

    def cross_set(self, keys, value):
        pass


def ships(found):
    return [(ship.name, ship.level, ship.mood, ship.speed) for ship in found]


def test_tab_of_the_dorm_ship_list():
    assert ship_list_tab(load('dorm_train.png')) == 'train'
    assert ship_list_tab(load('dorm_rest.png')) == 'rest'
    # The EXP popup of the dorm is white where the tabs are, it is not the ship list
    assert ship_list_tab(load('dorm_exp_popup.png')) is None
    assert ship_list_tab(load('picker.png')) is None


def test_reads_the_first_floor_of_the_dorm():
    found, slots = read_dorm_floor(load('dorm_train.png'), 'train')

    assert ships(found) == [('Victorious META', 109, 150, 40), ('Haruna', 99, 150, 40)]
    assert slots == 6


def test_reads_the_second_floor_of_the_dorm():
    found, slots = read_dorm_floor(load('dorm_rest.png'), 'rest')

    assert ships(found) == [('Hatakaze', 119, 150, 50), ('Oite', 119, 150, 50), ('Fusou META', 119, 150, 50),
                            ('Dmitri Donskoi', 100, 150, 50)]
    assert all(ship.place == 'rest' and ship.sig for ship in found)


def test_finds_the_rows_of_cards_of_the_picker():
    assert picker_row_tops(load('picker.png'))[:2] == [76, 303]
    # After a drag, the list does not move by whole rows
    assert picker_row_tops(load('picker_scrolled.png'))[:2] == [121, 348]


def test_reads_the_cards_of_the_picker():
    image = load('picker.png')
    first = read_picker_row(image, 76, 0)
    second = read_picker_row(image, 303, 1)

    assert first[0].remove
    hatakaze = first[1]
    assert (hatakaze.name, hatakaze.level, hatakaze.mood, hatakaze.fleet, hatakaze.selected) == \
           ('Hatakaze', 119, 150, 1, True)
    nana, gangut, whydah = second[0], second[5], second[6]
    assert (nana.name, nana.fleet, nana.selected, nana.truncated) == ('Nana Astar', 2, False, True)
    assert (gangut.name, gangut.level, gangut.fleet, gangut.submarine) == ('Gangut', 93, 1, False)
    # In the submarine fleet, her badge says fleet 1 too
    assert (whydah.name, whydah.mood, whydah.fleet, whydah.submarine) == ('Whydah', 119, 1, True)


def test_remove_card_is_found_at_the_top_of_the_list():
    first = read_picker_row(load('picker.png'), 76, 0)

    assert picker_is_top(first, {}, None)


def test_row_at_the_top_of_the_screen_is_the_first_of_the_list():
    first = [card(i, name) for i, name in enumerate(['Oite', 'Fusou META', 'Nevada META', 'Kawakaze ME', 'London',
                                                       'Hatakaze', 'Nana Astar'])]
    middle = [card(14 + i, name) for i, name in enumerate(['Alsace', 'Z52', 'Musashi', 'Little Illu', 'Hermes',
                                                             'Javelin', 'Arizona'])]
    again = [card(i, name) for i, name in enumerate(['0ite', 'Fusou META', 'Nevada META', 'Kawakaze ME', 'London',
                                                       'Hatakaze', 'Nana Astar'])]

    # A row of the middle of the list at the top of the screen
    assert not picker_is_top(middle, {0: first}, None)
    # The first row read before, OCR may differ a little
    assert picker_is_top(again, {0: first}, None)
    # Nothing read yet, a drag down that does not move the list
    assert picker_is_top(first, {}, again)
    assert not picker_is_top(first, {}, None)


def card(index, name, fleet=0, mood=150, level=100, submarine=False, truncated=False, remove=False):
    return PickerCard(row=index // 7, col=index % 7, name=name, level=level, mood=mood, fleet=fleet,
                      submarine=submarine, truncated=truncated, remove=remove)


def test_ships_in_fleets_end_with_two_cards_without_a_badge():
    residents = ['Hatakaze', 'Dmitri Donskoi']
    cards = {c.index: c for c in [
        card(0, '', remove=True), card(1, 'Hatakaze', fleet=1), card(2, 'Dmitri Dons', truncated=True),
        card(3, 'London (Ret', fleet=2), card(4, 'Missed badge'), card(5, 'Hermes', fleet=5)]}
    assert not picker_fleets_ended(cards, residents)

    cards[6] = card(6, 'Random')
    cards[7] = card(7, 'Another')
    assert picker_fleets_ended(cards, residents)


def test_update_follows_the_dorm_and_the_fleets():
    moods = ShipMoods(Config())
    long_ago = NOW - timedelta(days=4)
    moods.ships['Old ship'] = ShipMood('Old ship', time=long_ago)
    moods.ships['In a lineup'] = ShipMood('In a lineup', time=long_ago)
    # Out of the dorm since the last time
    moods.ships['Left the dorm'] = ShipMood('Left the dorm', mood=100, time=NOW - timedelta(hours=1), place='rest',
                                            speed=50, fleet=3)
    moods.lineups = {'Event2': {'1': ['In a lineup'], '2': []}}
    dorm = [
        # The dorm dropped a digit of 124
        DormShip(place='rest', name='Kawakaze META', level=115, mood=14, speed=50, sig=[1]),
        DormShip(place='train', name='lana Astar Deviluk', level=110, mood=150, speed=40),
        DormShip(place='train', name='yHieim', level=107, mood=120, speed=40),
    ]
    cards = [card(0, '', remove=True), card(1, 'Kawakaze ME', fleet=1, mood=124, truncated=True),
             card(2, 'Nana Astar', fleet=2, truncated=True), card(3, 'Hiei', fleet=2),
             card(4, 'London (Ret', fleet=2, mood=119, level=118, truncated=True),
             card(5, 'Whydah', fleet=1, mood=119, submarine=True), card(6, 'Random')]

    update_moods(moods, dorm, cards, NOW)

    # Named after the dock when it does not cut the name, after the dorm otherwise.
    # Ships not seen for days are forgotten, unless in a lineup.
    assert sorted(moods.ships) == ['Hiei', 'In a lineup', 'Kawakaze META', 'Left the dorm', 'London (Ret',
                                   'lana Astar Deviluk']
    left = moods.ships['Left the dorm']
    # Counted on the second floor until now, out of it from now on
    assert (left.mood, left.time, left.place, left.speed, left.fleet) == (150, NOW, 'dock', 20, 0)
    kawakaze = moods.ships['Kawakaze META']
    assert (kawakaze.mood, kawakaze.place, kawakaze.speed, kawakaze.fleet, kawakaze.time) == (124, 'rest', 50, 1, NOW)
    assert (moods.ships['Hiei'].place, moods.ships['Hiei'].fleet) == ('train', 2)
    london = moods.ships['London (Ret']
    assert (london.mood, london.place, london.speed, london.level, london.fleet) == (119, 'dock', 20, 118, 2)
    assert moods.read == NOW


def test_lineup_of_a_hard_mode_stage_is_matched_by_level_and_portrait():
    """
    Hatakaze, Oite and Fusou META are all at level 119, Hatakaze and Oite in fleet 1 of the lineup,
    Fusou META in fleet 2.
    """
    known = read_dorm_floor(load('dorm_rest.png'), 'rest')[0] + read_dorm_floor(load('dorm_train.png'), 'train')[0]
    ships_known = [ShipMood(ship.name, level=ship.level, sig=ship.sig) for ship in known]

    image = load('lineup.png')
    slots = [lineup_slot(fleet, position) for fleet in (1, 2) for position in range(SLOTS_PER_FLEET)]
    buttons = [Button(area=level_area(slot), color=(), button=(), name=f'LEVEL_{i}') for i, slot in enumerate(slots)]
    levels = Digit(buttons, letter=(255, 255, 255), threshold=128, name='LINEUP_LEVEL').ocr(image)
    signatures = [portrait_signature(crop(image, portrait_area(slot))) for slot in slots]

    assert levels == [109, 117, 99, 118, 119, 119, 119, 107, 93, 100, 115, 105]
    names = match_lineup(list(zip(levels, signatures)), ships_known)
    assert names[:6] == ['Victorious META', None, 'Haruna', None, 'Oite', 'Hatakaze']
    assert names[6:] == ['Fusou META', None, None, 'Dmitri Donskoi', None, None]
