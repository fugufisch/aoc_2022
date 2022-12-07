import pytest

from aoc_2022.day_06 import marker


@pytest.mark.parametrize(
    'data, output',
    (['data/day06/example.txt', 7],
     ['data/day06/input.txt', 1816]),
    indirect=['data']
)
def test_06_1(data, output):
    assert marker(data) == output


@pytest.mark.parametrize(
    'data, output',
    (['data/day06/example.txt', 19],
     ['data/day06/input.txt', 2625]),
    indirect=['data']
)
def test_06_2(data, output):
    assert marker(data, n=14) == output
