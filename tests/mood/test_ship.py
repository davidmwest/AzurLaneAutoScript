from datetime import datetime, timedelta

import pytest

from module.mood.ship import ShipMood, ShipMoods, name_similarity, portrait_similarity, tidy_name

# A tick of mood recovery starts every 6 minutes
T0 = datetime(2026, 10, 14, 8, 0, 0)


@pytest.mark.parametrize('read, known', [
    ('Kawakaze ME', 'Kawakaze META'),  # Cut by the dock
    ('lana Astar Deviluk', 'Nana Astar'),  # Cut at both sides by the dorm
    ('ana Astar Devilul', 'Nana Astar Deviluke'),
    ('littorio Cunibert', 'Vittorio Cu'),
    ('Ha run a', 'Haruna'),  # Spaces of OCR
    ('Z52', 'Z52'),
])
def test_same_ship_read_on_different_screens(read, known):
    assert name_similarity(read, known) > 0


@pytest.mark.parametrize('read, known', [
    ('Hiei', 'Haruna'),
    ('Z52', 'Z23'),  # Short names must match completely
    ('Oite', 'Hatakaze'),
    ('', 'Hiei'),
])
def test_different_ships(read, known):
    assert name_similarity(read, known) == 0


def test_complete_name_is_preferred_over_a_longer_one():
    assert name_similarity('Nevada', 'Nevada') > name_similarity('Nevada', 'Nevada META') > 0


@pytest.mark.parametrize('name, tidy', [
    ('Ha run a', 'Haruna'),
    ('F usou MET A', 'Fusou META'),
    ('G angut', 'Gangut'),
    ('C as sin', 'Cassin'),
    ('Als ace', 'Alsace'),
    ('U-55 7', 'U-557'),
    ('Kawakaze META', 'Kawakaze META'),
    ('Nana Astar', 'Nana Astar'),
    ('London (Ret', 'London (Ret'),
])
def test_tidy_name(name, tidy):
    assert tidy_name(name) == tidy


def test_mood_recovers_by_place_up_to_its_cap():
    rest = ShipMood('Hatakaze', mood=100, time=T0, place='rest', speed=50)
    dock = ShipMood('London', mood=100, time=T0, place='dock', speed=20)

    assert rest.at(T0 + timedelta(minutes=5)) == 100
    assert rest.at(T0 + timedelta(minutes=6)) == 105
    assert rest.at(T0 + timedelta(hours=1)) == 150
    assert dock.at(T0 + timedelta(hours=1)) == 119


def test_mood_above_the_cap_stays():
    ship = ShipMood('Azuchi', mood=144, time=T0, place='dock', speed=20)

    assert ship.at(T0 + timedelta(hours=3)) == 144


def test_battle_counts_recovery_first():
    ship = ShipMood('Oite', mood=100, time=T0, place='rest', speed=50)

    ship.fight(T0 + timedelta(minutes=12), 2)

    assert ship.mood == 108
    assert ship.time == T0 + timedelta(minutes=12)


def test_when_mood_reaches_a_target():
    ship = ShipMood('Oite', mood=40, time=T0, place='rest', speed=50)

    assert ship.when(40, T0) == T0
    # 10 more is 2 ticks
    assert ship.when(50, T0) == T0 + timedelta(minutes=12)


def test_mood_out_of_the_dorm_can_not_reach_above_119():
    ship = ShipMood('London', mood=100, time=T0, place='dock', speed=20)

    assert ship.when(121, T0) is None


class Config:
    def __init__(self, storage=None):
        self.storage = storage or {}

    def cross_get(self, keys, default=None):
        return self.storage if self.storage else default

    def cross_set(self, keys, value):
        self.storage = value


def test_ships_are_saved_and_read_back():
    config = Config()
    moods = ShipMoods(config)
    moods.ships['Oite'] = ShipMood('Oite', mood=123, time=T0, place='rest', speed=50, level=119, fleet=1,
                                   sig=[1, 2, 3])
    moods.lineups['Event2'] = {'1': ['Oite'], '2': []}
    moods.read = T0
    moods.save()

    again = ShipMoods(config)

    assert again.ships['Oite'] == moods.ships['Oite']
    assert again.lineups == {'Event2': {'1': ['Oite'], '2': []}}
    assert again.read == T0


def test_find_fleet_and_lineup():
    moods = ShipMoods(Config())
    for name, fleet in [('Kawakaze META', 1), ('Hiei', 2), ('Dmitri Donskoi', 0)]:
        moods.ships[name] = ShipMood(name, fleet=fleet)
    moods.lineups['Event2'] = {'1': ['Kawakaze META', 'Hiei'], '2': ['Dmitri Donskoi', 'Unknown ship']}

    assert moods.find('Kawakaze ME').name == 'Kawakaze META'
    assert moods.find('Hatakaze') is None
    assert moods.fleet(1) == ['Kawakaze META']
    assert moods.lineup('Event2', 1) == ['Kawakaze META', 'Hiei']
    # Ships no longer followed are left out
    assert moods.lineup('Event2', 2) == ['Dmitri Donskoi']
    assert moods.lineup('Event', 1) == []


def test_portrait_similarity_without_a_signature():
    assert portrait_similarity([1, 2, 3], None) == 0
    assert portrait_similarity([1, 2, 3], [1, 2, 3]) == pytest.approx(1)
