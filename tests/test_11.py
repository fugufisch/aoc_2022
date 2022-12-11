import pytest

from aoc_2022.day_11 import KeepAway


@pytest.mark.parametrize(
    'data, output',
    (['data/day11/example.txt', 10605],
     ['data/day11/input.txt', 12560]),
    indirect=['data']
)
def test_11_1(data, output):
    game = KeepAway(data)
    for _ in range(20):
        game.play_round()
    monkey_business = sorted([(i, monkey.inspection_count) for i, monkey in enumerate(game.monkeys)],
                             key=lambda x: x[1], reverse=True)[0:2]
    assert monkey_business[0][1] * monkey_business[1][1] == output


@pytest.mark.parametrize(
    'data, output',
    (['data/day11/example.txt', 2713310158],
     ['data/day11/input.txt', 12560]),
    indirect=['data']
)
def test_11_2(data, output):
    game = KeepAway(data, super_worried=True)
    for _ in range(10000):
        game.play_round()
    monkey_business = sorted([(i, monkey.inspection_count) for i, monkey in enumerate(game.monkeys)],
                             key=lambda x: x[1], reverse=True)[0:2]
    assert monkey_business[0][1] * monkey_business[1][1] == output
