# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import astar as mod  # noqa: E402


def test_straight_line_cost():
    g = astar.load_grid("data/grid.txt")
    p = astar.astar(g, (1, 1), (1, 5))
    assert astar.path_cost(g, p) == 4.0


def test_no_path():
    g = astar.load_grid("data/grid.txt")
    p = astar.astar(g, (0, 0), (7, 7))
    assert p == [] or p is None
