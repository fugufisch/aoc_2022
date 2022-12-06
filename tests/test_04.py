import pytest

from aoc_2022.day_04 import find_contained, parse


@pytest.mark.parametrize(
    'data, output',
    (['data/day04/example.txt', 2],
     ['data/day04/input.txt', 547]),
    indirect=['data']
)
def test_04_1(data, output):
    assert find_contained(parse(data)) == output

@pytest.mark.parametrize(
    'data, output',
    (['data/day04/example.txt', 4],
     ['data/day04/input.txt', 843]),
    indirect=['data']
)
def test_04_2(data, output):
    assert find_contained(parse(data), with_overlap=True) == output