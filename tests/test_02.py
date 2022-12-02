import pytest

from aoc_2022 import day_02


@pytest.fixture
def data_02():
    with open('data/day02/input.txt') as f:
        yield f.read()


def test_02_1(data_02):
    assert day_02.RPS().evaluate_strategy(data_02) == 15


def test_02_2(data_02):
    print(day_02.RPS().evaluate_strategy_advanced(data_02))
    assert day_02.RPS().evaluate_strategy_advanced(data_02) == 12
