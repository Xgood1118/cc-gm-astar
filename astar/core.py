# -*- coding: utf-8 -*-
"""动态障碍寻路"""

from dataclasses import dataclass


@dataclass
class Grid:
    """带障碍的格子地图。"""
    width: int
    height: int
    blocked: set


def Grid:
    """class"""
    raise NotImplementedError("Grid 尚未实现")


def astar(grid, start, goal):
    """寻路"""
    raise NotImplementedError("astar 尚未实现")


def smooth_path(grid, path):
    """路径平滑"""
    raise NotImplementedError("smooth_path 尚未实现")


def path_cost(grid, path):
    """算路径代价"""
    raise NotImplementedError("path_cost 尚未实现")


def load_grid(path):
    """读入与落盘辅助"""
    raise NotImplementedError("load_grid 尚未实现")

