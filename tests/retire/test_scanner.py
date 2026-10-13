import os

import cv2
import numpy as np

from module.config import server
from module.retire.dock import CARD_GRIDS
from module.retire.scanner import ShipScanner, StatusScanner

DATA = os.path.join(os.path.dirname(__file__), 'data')


def dock_choosing_a_ship_for_a_hard_mode_lineup():
    """
    ./data/dock_status_labels.png is the height of the status label of the 2nd and 3rd card in dock on the EN client,
    while choosing a ship for a hard mode lineup. The 2nd ship is "In Hard Mode", the 3rd is not.
    """
    labels = cv2.cvtColor(cv2.imread(os.path.join(DATA, 'dock_status_labels.png')), cv2.COLOR_BGR2RGB)
    image = np.zeros((720, 1280, 3), dtype=np.uint8)
    x, y = CARD_GRIDS[(1, 0)].area[:2]
    image[y + 120:y + 160, x:x + labels.shape[1]] = labels
    return image


def test_ship_in_the_hard_mode_lineup_is_not_free(monkeypatch):
    monkeypatch.setattr(server, 'server', 'en')
    image = dock_choosing_a_ship_for_a_hard_mode_lineup()

    status = StatusScanner()._scan(image)

    assert status[1] == 'in_hard_mode'
    assert status[2] == 'free'


def test_ship_in_the_hard_mode_lineup_is_not_a_candidate(monkeypatch):
    monkeypatch.setattr(server, 'server', 'en')
    image = dock_choosing_a_ship_for_a_hard_mode_lineup()
    scanner = ShipScanner(fleet=None, status='free')
    scanner.disable('level', 'emotion', 'rarity', 'fleet')

    free = [ship.button for ship in scanner.scan(image, output=False)]

    assert CARD_GRIDS[(1, 0)] not in free
    assert CARD_GRIDS[(2, 0)] in free
