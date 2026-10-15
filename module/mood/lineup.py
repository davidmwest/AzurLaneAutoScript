"""
Who is in the lineup of a stage that has its own, like hard mode.
The fleet selection of the stage shows portraits and levels but no names, the ships are matched with those
followed by module/mood/ship.py: by level, then by the colors of their portraits.
Ships of the lineup not followed yet are kept by level and portrait, the task DormRest finds them on the dock.
"""
import numpy as np

from module.base.button import Button
from module.base.timer import Timer
from module.base.utils import crop
from module.logger import logger
from module.map.lineup_rotation import SLOTS_PER_FLEET, lineup_slot
from module.mood.ship import DOCK_SPEED, ShipMood, ShipMoods, name_key, plausible_name, portrait_signature, \
    portrait_similarity
from module.ocr.ocr import Digit

# Portraits of a ship on two screens are this similar at least, see portrait_similarity().
# Different ships go up to 0.77 for two destroyers of a class, the best match is taken first.
PORTRAIT_MIN = 0.5
# Bonus of the exact level over a level off by one, the ship may have leveled up since she was read
SAME_LEVEL = 0.2
# A portrait drawn on screen, not a placeholder of a single color
PORTRAIT_DRAWN_STD = 20
# Ships known on the lineup of a task, it does not lose more at once
MATCHES_LOST_MAX = 2
# A card of the dock taken for a ship of a lineup not followed yet, among the many ships of the dock.
# The same ship scored 0.86 and 0.94, others 0.69 at most.
CARD_PORTRAIT_MIN = 0.75


def level_area(slot):
    """
    Args:
        slot (Button): See lineup_slot()

    Returns:
        tuple: The digits of "LV.109" above the portrait.
    """
    x1, y1, x2, y2 = slot.area
    return x1 + 14, y1 - 15, x2 + 1, y1 + 2


def portrait_area(slot):
    x1, y1, x2, y2 = slot.area
    return x1 - 36, y1 - 13, x2, y2 + 25


def match_portraits(slots, candidates, minimum):
    """
    Args:
        slots (list[tuple[int, list[int]]]): Level and portrait signature of each slot, level 0 if empty.
        candidates (list[tuple[Any, int, list[int] | tuple]]): Key, level and portrait signature of each candidate,
            or a tuple of signatures, the best one counts.
        minimum (float): Similarity of portraits needed.

    Returns:
        list: Key of the candidate in each slot, None if empty or not matched.
            Same level or one apart, best matches first, a candidate is in one slot only.
    """
    pairs = []
    for index, (level, signature) in enumerate(slots):
        if level <= 0:
            continue
        for key, candidate_level, candidate_signatures in candidates:
            if not candidate_level or abs(candidate_level - level) > 1:
                continue
            if not isinstance(candidate_signatures, tuple):
                candidate_signatures = (candidate_signatures,)
            similarity = max([portrait_similarity(signature, s) for s in candidate_signatures if s], default=0.)
            if similarity < minimum:
                continue
            score = similarity + (SAME_LEVEL if candidate_level == level else 0.)
            pairs.append((score, index, key))

    keys = [None] * len(slots)
    used = set()
    for score, index, key in sorted(pairs, key=lambda pair: -pair[0]):
        if keys[index] is None and key not in used:
            keys[index] = key
            used.add(key)
    return keys


def match_lineup(slots, ships):
    """
    Args:
        slots (list[tuple[int, list[int]]]): Level and portrait signature of each slot, level 0 if empty.
        ships (list[ShipMood]): Ships known.

    Returns:
        list[str]: Name for each slot, None if empty or not matched.
    """
    return match_portraits(slots, [(ship.name, ship.level, (ship.sig, ship.card_sig)) for ship in ships],
                           PORTRAIT_MIN)


def learn_lineup_ships(moods, cards, now):
    """
    Ships of a lineup out of the dorm and of the fleets are known by level and portrait only, see record_lineup().
    The picker of the dorm lists them after the ships in fleets, lowest mood first, once battles lowered it.

    Args:
        moods (ShipMoods):
        cards (list[PickerCard]): Cards of the picker, `ship` is set on those of the ships followed.
        now (datetime):

    Returns:
        list[str]: Names of the ships found.
    """
    assigned = {card.ship for card in cards if card.ship}
    free = {card.index: card for card in cards
            if not card.remove and not card.ship and not card.fleet and not card.submarine
            and card.level and card.sig and len(name_key(card.name)) >= 2}
    found = []
    for task in list(moods.unknown):
        slots = moods.unknown[task]
        keys = match_portraits([(slot['level'], slot['sig']) for slot in slots],
                               [(index, card.level, card.sig) for index, card in free.items()], CARD_PORTRAIT_MIN)
        remaining = []
        for slot, key in zip(slots, keys):
            if key is None:
                remaining.append(slot)
                continue
            card = free[key]
            if not card.ship:
                known = moods.ships.get(card.name)
                if known is not None and known.name in assigned:
                    # Another card is that ship, two of the same name
                    remaining.append(slot)
                    continue
                if known is None and not plausible_name(card.name):
                    # A name misread, she is found another time
                    remaining.append(slot)
                    continue
                # A ship of that name out of the dorm and of the fleets is her
                if known is None:
                    known = ShipMood(name=card.name)
                    moods.ships[card.name] = known
                known.card_sig = card.sig or known.card_sig
                known.mood, known.time, known.place, known.speed = card.mood, now, 'dock', DOCK_SPEED
                # The portrait of the lineup matches best on the next sortie
                known.level, known.fleet, known.sig = card.level, 0, known.sig or slot['sig']
                card.ship = known.name
                assigned.add(known.name)
                found.append(known.name)
            names = moods.lineups.setdefault(task, {}).setdefault(str(slot['fleet']), [])
            if card.ship not in names:
                names.append(card.ship)
            logger.info(f'Lineup of {task}: fleet {slot["fleet"]} has {card.ship}, Lv.{card.level}, '
                        f'mood {card.mood}, found on the dock')
        if remaining:
            moods.unknown[task] = remaining
        else:
            moods.unknown.pop(task)
    return found


def task_moods(main):
    """
    Args:
        main (ModuleBase):

    Returns:
        ShipMoods: The ships followed, None if the task DormRest is not enabled.
            The same the battles of the task count mood for, not another copy that would save over them.
    """
    if not main.config.is_task_enabled('DormRest'):
        return None
    emotion = getattr(main, 'emotion', None)
    moods = getattr(emotion, 'moods', None)
    if isinstance(moods, ShipMoods):
        return moods
    return ShipMoods(main.config)


def forget_lineup(main):
    """
    The stage of the task uses the common fleets, a lineup seen before for the task is no longer used.

    Args:
        main (ModuleBase):

    Pages:
        in: FLEET_PREPARATION, of a stage that uses the common fleets
    """
    moods = task_moods(main)
    if moods is None:
        return
    task = getattr(main.config.task, 'command', '')
    if task in moods.lineups or task in moods.unknown:
        logger.info(f'Stage of {task} uses the common fleets, its lineup is forgotten')
        moods.lineups.pop(task, None)
        moods.unknown.pop(task, None)
        moods.lineup_levels.pop(task, None)
        moods.save()


def record_lineup(main):
    """
    Remember who is in the lineup on the fleet selection of a stage, for the task running.

    Args:
        main (ModuleBase):

    Returns:
        bool: If the lineup is fully known.

    Pages:
        in: FLEET_PREPARATION, of a stage that has its own lineup
    """
    config = main.config
    moods = task_moods(main)
    if moods is None:
        return False

    slots = [lineup_slot(fleet, position) for fleet in (1, 2) for position in range(SLOTS_PER_FLEET)]
    buttons = [Button(area=level_area(slot), color=(), button=(), name=f'{slot.name}_LEVEL') for slot in slots]
    ocr = Digit(buttons, letter=(255, 255, 255), threshold=128, name='LINEUP_LEVEL')
    # Portraits come after the levels, wait for them
    timeout = Timer(3, count=6).start()
    while 1:
        image = main.device.image
        levels = ocr.ocr(image)
        areas = [crop(image, portrait_area(slot), copy=False) for slot, level in zip(slots, levels) if level > 0]
        if all(float(np.std(area)) > PORTRAIT_DRAWN_STD for area in areas) or timeout.reached():
            break
        main.device.screenshot()
    signatures = [portrait_signature(crop(image, portrait_area(slot))) for slot in slots]
    names = match_lineup(list(zip(levels, signatures)), list(moods.ships.values()))

    lineup, unknown = {}, []
    for index, (level, signature, name) in enumerate(zip(levels, signatures, names)):
        fleet = index // SLOTS_PER_FLEET + 1
        names_of_fleet = lineup.setdefault(str(fleet), [])
        if level <= 0:
            continue
        if name is None:
            unknown.append({'fleet': fleet, 'level': level, 'sig': signature})
        else:
            names_of_fleet.append(name)

    task = getattr(config.task, 'command', '')
    logger.attr('Lineup', f'{task} {lineup}')
    before = moods.lineups.get(task, {})
    known_before = sum(len(names) for names in before.values())
    known_now = sum(len(names) for names in lineup.values())
    levels_before = moods.lineup_levels.get(task, [])
    same_lineup = len(levels_before) == len(levels) \
        and sum(abs(a - b) <= 1 for a, b in zip(levels_before, levels)) >= len(levels) - 2
    if same_lineup and known_now < known_before - MATCHES_LOST_MAX:
        # A lineup changes a ship or two at a time, many ships lost at once is a screen read badly
        logger.warning(f'Lineup of {task} read with {known_now} ships known instead of {known_before}, '
                       f'the one read before is kept')
        return False
    moods.lineups[task] = lineup
    moods.lineup_levels[task] = [int(level) for level in levels]
    if unknown:
        # Out of the dorm and of the fleets, the task DormRest finds them on the dock once they are low on mood
        logger.info(f'Lineup ships not followed yet, fleet and level: '
                    f'{[(slot["fleet"], slot["level"]) for slot in unknown]}')
        moods.unknown[task] = unknown
    else:
        moods.unknown.pop(task, None)
    moods.save()
    return not unknown
