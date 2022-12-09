import pytest

from aoc_2022.day_09 import move


@pytest.mark.parametrize(
    'data, output',
    (['data/day09/example.txt', 13],
     ['data/day09/input.txt', 6044]),
    indirect=['data']
)
def test_09_1(data, output):
    assert move(data) == output


@pytest.mark.parametrize(
    'data, output',
    (['data/day09/example_2.txt', 36],
     ['data/day09/input.txt', 6044]),
    indirect=['data']
)
def test_09_2(data, output):
    assert move(data, n_knots=10) == output
