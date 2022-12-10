import pytest

from aoc_2022.day_10 import Device


@pytest.mark.parametrize(
    'data, output',
    (['data/day10/example.txt', 13140],
     ['data/day10/input.txt', 12560]),
    indirect=['data']
)
def test_10_1(data, output):
    dev = Device()
    assert dev.execute_seq(data) == output

@pytest.mark.parametrize(
    'data, output',
    (['data/day10/example.txt', 13140],
     ['data/day10/input.txt', 12560]),
    indirect=['data']
)
def test_10_2(data, output):
    dev = Device()
    dev.execute_seq(data)
    print(dev.screen)
