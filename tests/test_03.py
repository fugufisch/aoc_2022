import pytest

from aoc_2022.day_03 import get_sum


@pytest.fixture(params=["path"])
def data(request):
    with open(request.param) as f:
        yield f.read()


@pytest.mark.parametrize(
    'data, output',
    (['data/day03/example.txt', 157],
     ['data/day03/input.txt', 8515]),
    indirect=['data']
)
def test_03_1(data, output):
    assert get_sum(data) == output


@pytest.mark.parametrize(
    'data, output',
    (['data/day03/example.txt', 70],
     ['data/day03/input.txt', 8515]),
    indirect=['data']
)
def test_03_2(data, output):
    assert get_sum(data, part=2) == output
