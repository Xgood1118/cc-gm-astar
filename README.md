# 动态障碍寻路

一个在障碍会变化的地图上重规划、并保证路径代价最优的寻路器

## 保留签名

- `Grid`
- `astar(grid, start, goal)`
- `smooth_path(grid, path)`
- `path_cost(grid, path)`

## 自测

```
python -m pytest tests -q
python -m astar.cli data/grid.txt --from 1,1 --to 6,6 --out path.json
```
