import pytest

from aoc_2022 import day_02


@pytest.fixture(params=["path"])
def data_02(request):
    with open(request.param) as f:
        yield f.read()


@pytest.mark.parametrize(
    'data_02, output',
    (['data/day02/example.txt', 15],
     ['data/day02/input.txt', 11386]),
    indirect=['data_02']
)
def test_02_1(data_02, output):
    assert day_02.RPS().evaluate_strategy(data_02) == output


@pytest.mark.parametrize(
    'data_02, output',
    (['data/day02/example.txt', 12],
     ['data/day02/input.txt', 13600]),
    indirect=['data_02']
)
def test_02_2(data_02, output):
    assert day_02.RPS().evaluate_strategy_advanced(data_02) == output
