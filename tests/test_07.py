import pytest

from aoc_2022.day_07 import FileSystem


@pytest.mark.parametrize(
    'data, output',
    (['data/day07/example.txt', 95437],
     ['data/day07/input.txt', 911275]),
    indirect=['data']
)
def test_07_1(data, output):
    fs = FileSystem(data)
    fs.du(fs.dir_tree['/'], '/')
    assert sum([y for y in fs.sizes if y <= 100000]) == output


@pytest.mark.parametrize(
    'data, output',
    (['data/day07/example.txt', 24933642],
     ['data/day07/input.txt', 6183184]),
    indirect=['data']
)
def test_07_1(data, output):
    fs = FileSystem(data)
    fs.du(fs.dir_tree['/'], '/')
    root = max(fs.sizes)
    big_dirs = [x for x in fs.sizes
                if (70_000_000 - root + x >= 30_000_000)]
    assert min(big_dirs) == output
