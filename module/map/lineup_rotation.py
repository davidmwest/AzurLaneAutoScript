from module.base.button import Button
from module.equipment import assets as equipment_assets
from module.logger import logger
from module.map.assets import FLEET_PREPARATION
from module.retire.assets import DOCK_CHECK
from module.retire.dock import Dock
from module.retire.scanner import ShipScanner

# Ships of a fleet as the map lists them: main fleet first, then vanguard
SLOTS_PER_FLEET = 6


def lineup_slot(fleet, position):
    """
    Where a ship is on the fleet selection of a stage that has its own lineup, such as hard mode.
    There are buttons for the first and the last ship of the main fleet and of the vanguard,
    the ship between them is half way.

    Args:
        fleet (int): 1 or 2
        position (int): 0 to 5, main fleet first, then vanguard

    Returns:
        Button:
    """
    row = 'BACKLINE' if position < 3 else 'VANGUARD'
    first = getattr(equipment_assets, f'FLEET_{fleet}_{row}_1')
    last = getattr(equipment_assets, f'FLEET_{fleet}_{row}_3')
    step = position % 3
    area = tuple(int(a + (b - a) * step / 2) for a, b in zip(first.button, last.button))
    return Button(area=area, color=first.color, button=area, name=f'FLEET_{fleet}_{row}_{step + 1}')


def slots_to_rotate(lv_fleets, level):
    """
    Args:
        lv_fleets (dict[int, list[int]]): Levels last seen in each fleet, -1 if unknown.
        level (int): Ships at this level and above are to be replaced.

    Returns:
        list[tuple[int, int]]: (fleet, position)
    """
    return [
        (fleet, position)
        for fleet, levels in sorted(lv_fleets.items())
        for position, lv in enumerate(levels[:SLOTS_PER_FLEET])
        if lv >= level
    ]


class LineupRotation(Dock):
    """
    Replace ships in the lineup of a stage, on the fleet selection of the stage.
    Who comes in is up to the dock: the first ship that fits, in the order and with the filters asked for.
    """

    def rotation_candidates(self):
        """
        Returns:
            list[Ship]: Ships that may come in, in the order of the dock.

        Pages:
            in: DOCK_CHECK, choosing a ship for a slot
        """
        self.dock_favourite_set(self.config.ShipRotation_Favourite, wait_loading=False)
        self.dock_sort_method_dsc_set(self.config.ShipRotation_Descending, wait_loading=False)
        # not_level_max: a ship at its level cap gains nothing, limit break or awakening comes first
        self.dock_filter_set(
            sort=self.config.ShipRotation_Sort,
            faction=self.config.ShipRotation_Faction,
            rarity=self.config.ShipRotation_Rarity,
            extra='not_level_max',
        )
        level = (max(self.config.ShipRotation_MinLevel, 1), self.config.ShipRotation_Level - 1)
        # Ships of the common fleets may come in too if asked, lineups of stages are apart from them
        fleet = None if self.config.ShipRotation_FromFleets else 0
        scanner = ShipScanner(level=level, fleet=fleet, status='free')
        scanner.disable('rarity', 'emotion')
        return scanner.scan(self.device.image, output=True)

    def rotate(self, fleet, position):
        """
        Replace one ship of the lineup.

        Args:
            fleet (int): 1 or 2
            position (int): 0 to 5, main fleet first, then vanguard

        Returns:
            bool: If replaced. False if no ship fits, the lineup stays as it is then.

        Pages:
            in: FLEET_PREPARATION
            out: FLEET_PREPARATION
        """
        slot = lineup_slot(fleet, position)
        logger.hr(f'Rotate {slot}', level=2)
        self.ship_info_enter(click_button=slot, check_button=DOCK_CHECK, long_click=False, skip_first_screenshot=False)

        candidates = self.rotation_candidates()
        if not candidates:
            logger.warning(f'No ship to replace {slot} with, check the ShipRotation settings')
            self.dock_reset()
            self.ui_back(check_button=FLEET_PREPARATION)
            return False

        ship = candidates[0]
        logger.info(f'Replace {slot} with a ship at level {ship.level}')
        self.dock_select_one(ship.button)
        self.dock_reset()
        self.dock_select_confirm(check_button=FLEET_PREPARATION)
        return True
