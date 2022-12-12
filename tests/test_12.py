import pytest

from aoc_2022.day_12 import build_graph, dijkstra


@pytest.mark.parametrize(
    'data, output',
    (['data/day12/example.txt', 31],
     ['data/day12/input.txt', 497]),
    indirect=['data']
)
def test_12_1(data, output):
    graph, start, end = build_graph(data)
    shortest_paths, paths = dijkstra(graph, start)
    assert shortest_paths[end] == output


@pytest.mark.parametrize(
    'data, output',
    (['data/day12/example.txt', 29],
     ['data/day12/input.txt', 12560]),
    indirect=['data']
)
def test_12_2(data, output):
    graph, start, end = build_graph(data, reversed=True)
    shortest_paths, paths = dijkstra(graph, start)
    assert min([shortest_paths[e] for e in end]) == output
