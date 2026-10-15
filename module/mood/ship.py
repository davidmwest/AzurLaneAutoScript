"""
Mood of single ships. The dorm shows it exactly, from there on it is followed:
recovery where the ship is, and the battles of the fleet she is in.

Ships are known by their names, read with OCR. Screens cut long names differently, see name_similarity().
Screens that show no name, like the lineup of a hard mode stage, are matched by level and portrait colors.
"""
import re
from dataclasses import dataclass, field
from datetime import datetime
from math import ceil
from typing import Dict, List, Optional

import cv2
import numpy as np

# Mood recovers every 6 minutes, by a tenth of the speed per hour
TICK = 360
MOOD_MAX = 150
# Out of the dorm, mood recovers up to here and no further
DOCK_MOOD_MAX = 119
DOCK_SPEED = 20
# Where a ship is: on the second floor of the dorm, on the first floor, or anywhere else
PLACES = ('rest', 'train', 'dock')
# Two portraits of the same screen are the same ship from this similarity, see ShipMoods.find_by_portrait()
SAME_SHIP_PORTRAIT = 0.95
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def name_key(name):
    """
    'Kawakaze ME..' -> 'kawakazeme', 'London (Retrofit)' -> 'londonretrofit'
    """
    return re.sub(r'[^a-z0-9]', '', str(name).lower())


def tidy_name(name):
    """
    OCR puts spaces inside words: 'Ha run a' -> 'Haruna', 'F usou MET A' -> 'Fusou META', 'U-55 7' -> 'U-557'.
    Words of names start with a capital letter, what comes after a space in lowercase or as a digit
    continues the word.
    """
    words = []
    for token in str(name).split():
        if words and (token[0].islower() or token[0].isdigit()
                      or (len(words[-1]) == 1 and words[-1].isupper())
                      or (token.isupper() and len(token) <= 2 and words[-1].isupper())):
            words[-1] += token
        else:
            words.append(token)
    return ' '.join(words)


def plausible_name(name):
    """
    A screen read before it is drawn gives names like 'NN-d- AMET' or 'me～u METn'.

    Returns:
        bool: If a name read can be the name of a new ship.
    """
    name = str(name).strip()
    # Z52 is a ship
    if len(re.findall(r'[A-Za-zÀ-ÿ0-9]', name)) < 3 or not re.search(r'[A-Za-zÀ-ÿ]', name):
        return False
    if re.search(r"[^A-Za-zÀ-ÿ0-9 ().'&!?-]", name):
        return False
    # Hyphens are inside words, like in U-557
    if re.search(r'--|^-|-$|-\s|\s-', name):
        return False
    return True


def common_substring(a, b):
    """
    Returns:
        int: Length of the longest common substring.
    """
    best = 0
    previous = [0] * (len(b) + 1)
    for i in range(1, len(a) + 1):
        current = [0] * (len(b) + 1)
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                current[j] = previous[j - 1] + 1
                best = max(best, current[j])
        previous = current
    return best


def name_similarity(read, known):
    """
    The dock cuts long names at the end ("Kawakaze ME.."), the dorm at both sides of the card
    ("lana Astar Deviluk"), OCR adds spaces and drops letters at the edges.

    Args:
        read (str): Name read on a screen.
        known (str): Name of a ship already known.

    Returns:
        float: 0 if not the same ship, above 1 if probably the same. A complete match scores 1.1,
            a shorter name that is all in the longer one scores less the shorter it is.
    """
    a, b = name_key(read), name_key(known)
    if not a or not b:
        return 0.
    if a == b:
        return 1.1
    short, long = sorted([a, b], key=len)
    # Names of 3 letters or less, like Z52, must match completely
    if len(short) < 4:
        return 0.
    common = common_substring(short, long)
    if common < 4 or common / len(short) < 0.8:
        return 0.
    return common / len(short) + 0.1 * len(short) / len(long)


def portrait_signature(image):
    """
    Colors of a ship portrait, to tell ships apart on screens that show no name.

    Args:
        image (np.ndarray): RGB portrait.

    Returns:
        list[int]: Hue-saturation histogram, 18x8 bins scaled to 0-255.
    """
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    hist = cv2.calcHist([hsv], [0, 1], None, [18, 8], [0, 180, 0, 256]).flatten()
    hist = hist / max(float(hist.max()), 1.) * 255
    return [int(round(v)) for v in hist]


def portrait_similarity(a, b):
    """
    Returns:
        float: Correlation of two signatures, 1 for the same colors, 0 if a signature is missing.
    """
    if not a or not b or len(a) != len(b):
        return 0.
    return float(cv2.compareHist(np.array(a, dtype=np.float32), np.array(b, dtype=np.float32), cv2.HISTCMP_CORREL))


def parse_time(value):
    if isinstance(value, datetime):
        return value
    try:
        return datetime.strptime(str(value), TIME_FORMAT)
    except ValueError:
        return None


@dataclass
class ShipMood:
    name: str
    # Mood at `time`
    mood: int = 0
    time: datetime = field(default_factory=lambda: datetime.now().replace(microsecond=0))
    place: str = 'dock'
    # Recovery per hour where she is, the dorm shows it
    speed: int = DOCK_SPEED
    level: int = 0
    # Common fleet 1 to 6 she is in, 0 for none
    fleet: int = 0
    # See portrait_signature(), of her portrait in the dorm, or else on the dock
    sig: Optional[List[int]] = None
    # Of her card on the dock, compared with cards only
    card_sig: Optional[List[int]] = None

    @property
    def cap(self):
        return MOOD_MAX if self.place in ('rest', 'train') else DOCK_MOOD_MAX

    def at(self, now):
        """
        Args:
            now (datetime):

        Returns:
            int: Mood at `now`, recovered since `time`.
        """
        # Above the cap of where she is, mood is kept but does not go up
        if self.mood >= self.cap:
            return self.mood
        ticks = max(int(now.timestamp()) // TICK - int(self.time.timestamp()) // TICK, 0)
        return min(self.mood + int(ticks * self.speed / 10), self.cap)

    def fight(self, now, cost):
        """
        A battle of her fleet.

        Args:
            now (datetime):
            cost (int): Mood lost.
        """
        self.mood = max(self.at(now) - cost, 0)
        self.time = now.replace(microsecond=0)

    def when(self, target, now):
        """
        Args:
            target (int): Mood to reach.
            now (datetime):

        Returns:
            datetime: When the mood reaches `target`, `now` if it already has,
                None if it can not where she is, like above 119 out of the dorm.
        """
        current = self.at(now)
        if current >= target:
            return now
        if target > self.cap or self.speed <= 0:
            return None
        ticks = ceil((target - current) / (self.speed / 10))
        return datetime.fromtimestamp((int(now.timestamp()) // TICK + ticks) * TICK)

    def to_dict(self):
        data = {
            'mood': int(self.mood),
            'time': self.time.strftime(TIME_FORMAT),
            'place': self.place,
            'speed': int(self.speed),
            'level': int(self.level),
            'fleet': int(self.fleet),
        }
        if self.sig:
            data['sig'] = list(self.sig)
        if self.card_sig:
            data['card_sig'] = list(self.card_sig)
        return data

    @classmethod
    def from_dict(cls, name, data):
        return cls(
            name=name,
            mood=int(data.get('mood', 0)),
            time=parse_time(data.get('time')) or datetime.now().replace(microsecond=0),
            place=data.get('place', 'dock') if data.get('place') in PLACES else 'dock',
            speed=int(data.get('speed', DOCK_SPEED)),
            level=int(data.get('level', 0)),
            fleet=int(data.get('fleet', 0)),
            sig=data.get('sig') or None,
            card_sig=data.get('card_sig') or None,
        )


class ShipMoods:
    """
    The ships Purin follows, kept in the storage of the DormRest task:
        {
            'read': when the dorm was read last,
            'ships': {name: ShipMood.to_dict()},
            'lineups': {task: {'1': [names], '2': [names]}}, lineups of stages that have their own,
            'unknown': {task: [{'fleet': 1, 'level': 100, 'sig': [...]}]}, ships of those lineups
                not followed yet, known by level and portrait only,
            'lineup_levels': {task: [levels of the 12 slots]}, when the lineup was read
        }
    """
    KEYS = 'DormRest.Storage.Storage'

    def __init__(self, config):
        """
        Args:
            config (AzurLaneConfig):
        """
        self.config = config
        data = config.cross_get(keys=self.KEYS, default={}) or {}
        self.read = parse_time(data.get('read'))
        self.ships: Dict[str, ShipMood] = {
            name: ShipMood.from_dict(name, ship) for name, ship in data.get('ships', {}).items()}
        self.lineups: Dict[str, Dict[str, List[str]]] = data.get('lineups', {}) or {}
        self.unknown: Dict[str, List[dict]] = data.get('unknown', {}) or {}
        # Levels of the slots of a lineup when it was read, to tell the same lineup read again
        self.lineup_levels: Dict[str, List[int]] = data.get('lineup_levels', {}) or {}

    def to_dict(self):
        return {
            'read': self.read.strftime(TIME_FORMAT) if self.read else '',
            'ships': {name: ship.to_dict() for name, ship in self.ships.items()},
            'lineups': self.lineups,
            'unknown': self.unknown,
            'lineup_levels': self.lineup_levels,
        }

    def save(self):
        self.config.cross_set(keys=self.KEYS, value=self.to_dict())

    def find(self, name):
        """
        Args:
            name (str): Name read on a screen.

        Returns:
            ShipMood: The known ship with the most similar name, None if none is similar.
        """
        best, score = None, 0.
        for ship in self.ships.values():
            similarity = name_similarity(name, ship.name)
            if similarity > score:
                best, score = ship, similarity
        return best

    def find_by_portrait(self, level, sig, card=False, exclude=()):
        """
        A ship whose name was misread, told by her level and portrait.
        The same ship on the same screen scores 0.98 and more, two destroyers of a class at the same level 0.86.

        Args:
            level (int): Level read, she may be a level above.
            sig (list[int]): Portrait signature read.
            card (bool): If the portrait is of a card on the dock, compared with the cards seen before.
            exclude: Names of the ships told apart already.

        Returns:
            ShipMood: The known ship with the most similar portrait, None if none is similar enough.
        """
        if not sig or not level:
            return None
        best, score = None, SAME_SHIP_PORTRAIT
        for ship in self.ships.values():
            known = (ship.card_sig or ship.sig) if card else ship.sig
            if ship.name in exclude or not known or not ship.level or abs(ship.level - level) > 1:
                continue
            similarity = portrait_similarity(sig, known)
            if similarity > score:
                best, score = ship, similarity
        return best

    def fleet(self, number):
        """
        Args:
            number (int): Common fleet 1 to 6.

        Returns:
            list[str]: Names of the ships in it.
        """
        return [ship.name for ship in self.ships.values() if ship.fleet == number]

    def lineup(self, task, index):
        """
        Args:
            task (str):
            index (int): 1 or 2.

        Returns:
            list[str]: Names of the ships in a fleet of the lineup of a stage, those followed.
        """
        return [name for name in self.lineups.get(task, {}).get(str(index), []) if name in self.ships]

    def in_lineups(self):
        """
        Returns:
            set[str]: Names of the ships in the lineup of any stage.
        """
        return {name for lineup in self.lineups.values() for names in lineup.values() for name in names}

    def ships_of(self, names):
        return [self.ships[name] for name in names if name in self.ships]
