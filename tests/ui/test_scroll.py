import numpy as np
import pytest

from module.ui.scroll import best_interval, best_window


@pytest.mark.parametrize('score, expected', [
    ([-1, 2, 3, -1], (1, 3)),
    ([2, 3], (0, 2)),
    # A weak gap is bridged when what follows is worth more than the gap costs
    ([5, -1, 5, -9, 1], (0, 3)),
    # A strong gap is not
    ([5, -9, 6], (2, 3)),
    ([-1, -2], (0, 0)),
    ([0, 0], (0, 0)),
    ([], (0, 0)),
])
def test_best_interval(score, expected):
    assert best_interval(np.array(score, dtype=np.float32)) == expected


@pytest.mark.parametrize('score, length, expected', [
    ([-1, 2, 3, -1], 2, 1),
    ([-2, 2, 3, -1], 3, 1),
    ([-1, 2, 3, -1], 4, 0),
    ([5, -9, 6], 1, 2),
    # The first of equally good ones
    ([0, 0, 0], 2, 0),
    ([-3, -1, -2], 1, 1),
])
def test_best_window(score, length, expected):
    assert best_window(np.array(score, dtype=np.float32), length) == expected
