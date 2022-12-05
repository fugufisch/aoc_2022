import pytest

from aoc_2022.day_05 import get_tops, move, parse


@pytest.mark.parametrize(
    'data, output',
    (['data/day05/example.txt', 'CMZ'],
     ['data/day05/input.txt', 'QGTHFZBHV']),
    indirect=['data']
)
def test_05_1(data, output):
    assert get_tops(move(*parse(data))) == output


@pytest.mark.parametrize(
    'data, output',
    (['data/day05/example.txt', 'MCD'],
     ['data/day05/input.txt', 'MGDMPSZTM']),
    indirect=['data']
)
def test_05_2(data, output):
    assert get_tops(move(*parse(data), multiple=True)) == output
