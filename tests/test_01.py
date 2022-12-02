import pytest

from aoc_2022 import day_01


@pytest.fixture
def data_01():
    with open('data/day01/input.txt') as f:
        yield f.read()


def test_day_01_1(data_01):
    calory_list = day_01.parse_calories(data_01)
    print(f'\nResult: {sum(day_01.top_calories(calory_list, n=1))}')


def test_day_01_2(data_01):
    calory_list = day_01.parse_calories(data_01)
    print(f'\nResult: {sum(day_01.top_calories(calory_list))}')
