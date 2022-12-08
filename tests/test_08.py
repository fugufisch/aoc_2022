from itertools import chain

import pytest

from aoc_2022.day_08 import get_scenic_score, get_visibility, parse


@pytest.mark.parametrize(
    'data, output',
    (['data/day08/example.txt', 21],
     ['data/day08/input.txt', 911275]),
    indirect=['data']
)
def test_08_1(data, output):
    grid = parse(data)
    vis_x = [get_visibility(x) for x in grid[1:-1]]
    transposed = list(zip(*grid))
    vis_y = [get_visibility(x) for x in transposed[1:-1]]
    vis = [x or y for x, y in zip(chain.from_iterable(vis_x), chain.from_iterable(zip(*vis_y)))]
    vis_count = sum(vis) + len(grid) * 4 - 4
    assert vis_count == output


@pytest.mark.parametrize(
    'data, output',
    (['data/day08/example.txt', 8],
     ['data/day08/input.txt', 496650]),
    indirect=['data']
)
def test_08_2(data, output):
    grid = parse(data)

    assert get_scenic_score(grid) == output
