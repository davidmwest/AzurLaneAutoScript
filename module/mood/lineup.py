"""
Who is in the lineup of a stage that has its own, like hard mode.
The fleet selection of the stage shows portraits and levels but no names, the ships are matched with those
followed by module/mood/ship.py: by level, then by the colors of their portraits.
"""
from module.base.button import Button
from module.base.utils import crop
from module.logger import logger
from module.map.lineup_rotation import SLOTS_PER_FLEET, lineup_slot
from module.mood.ship import ShipMoods, portrait_signature, portrait_similarity
from module.ocr.ocr import Digit

# A ship without a portrait to compare scores this
SIMILARITY_UNKNOWN = 0.4
# Bonus of the exact level over a level off by one, the ship may have leveled up since she was read
SAME_LEVEL = 0.2
MATCH_MIN = 0.3


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


def match_lineup(slots, ships):
    """
    Args:
        slots (list[tuple[int, list[int]]]): Level and portrait signature of each slot, level 0 if empty.
        ships (list[ShipMood]): Ships known.

    Returns:
        list[str]: Name for each slot, None if empty or not matched.
    """
    pairs = []
    for index, (level, signature) in enumerate(slots):
        if level <= 0:
            continue
        for ship in ships:
            if not ship.level or abs(ship.level - level) > 1:
                continue
            score = portrait_similarity(signature, ship.sig) if ship.sig else SIMILARITY_UNKNOWN
            if ship.level == level:
                score += SAME_LEVEL
            pairs.append((score, index, ship.name))

    names = [None] * len(slots)
    used = set()
    for score, index, name in sorted(pairs, key=lambda pair: -pair[0]):
        if score < MATCH_MIN:
            break
        if names[index] is None and name not in used:
            names[index] = name
            used.add(name)
    return names


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
    if task in moods.lineups:
        logger.info(f'Stage of {task} uses the common fleets, its lineup is forgotten')
        moods.lineups.pop(task)
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
    if not moods.ships:
        logger.info('No ship known yet, the task DormRest reads them in the dorm')
        return False

    image = main.device.image
    slots = [lineup_slot(fleet, position) for fleet in (1, 2) for position in range(SLOTS_PER_FLEET)]
    buttons = [Button(area=level_area(slot), color=(), button=(), name=f'{slot.name}_LEVEL') for slot in slots]
    levels = Digit(buttons, letter=(255, 255, 255), threshold=128, name='LINEUP_LEVEL').ocr(image)
    signatures = [portrait_signature(crop(image, portrait_area(slot))) for slot in slots]
    names = match_lineup(list(zip(levels, signatures)), list(moods.ships.values()))

    lineup = {}
    known = True
    for fleet in (1, 2):
        part = slice((fleet - 1) * SLOTS_PER_FLEET, fleet * SLOTS_PER_FLEET)
        fleet_names = [name for level, name in zip(levels[part], names[part]) if level > 0]
        if any(name is None for name in fleet_names):
            # Ships out of the dorm and of the fleets are not known, they are left out
            known = False
            logger.warning(f'Lineup fleet {fleet}: ships at levels {levels[part]} are not all known, '
                           f'matched {names[part]}')
        lineup[str(fleet)] = [name for name in fleet_names if name is not None]

    task = getattr(config.task, 'command', '')
    logger.attr('Lineup', f'{task} {lineup}')
    if moods.lineups.get(task) != lineup:
        moods.lineups[task] = lineup
        moods.save()
    return known
