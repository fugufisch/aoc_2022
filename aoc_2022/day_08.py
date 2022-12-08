from copy import copy
from typing import List


def parse(data: str):
    grid = []
    for row in data.split("\n"):
        grid.append([int(x) for x in row])
    return grid


def get_visibility(arr: List[int]) -> List[bool]:
    vis_arr = []
    for i in range(1, len(arr) - 1):
        vis_arr.append(max(arr[0:i]) < arr[i] or max(arr[i + 1:]) < arr[i])
    return vis_arr


def get_scenic_score(grid):
    scenic_scores = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            tree_height = grid[i][j]
            top = [grid[x][j] < tree_height for x in reversed(range(0, i))]
            bottom = [grid[x][j] < tree_height for x in range(i + 1, len(grid))]
            left = [grid[i][x] < tree_height for x in reversed(range(0, j))]
            right = [grid[i][x] < tree_height for x in range(j + 1, len(grid))]

            top_dist = top.index(False) + 1 if False in top else len(top)
            bottom_dist = bottom.index(False) + 1 if False in bottom else len(bottom)
            left_dist = left.index(False) + 1 if False in left else len(left)
            right_dist = right.index(False) + 1 if False in right else len(right)

            scenic_score = top_dist * bottom_dist * left_dist * right_dist
            scenic_scores.append(scenic_score)
    return max(scenic_scores)