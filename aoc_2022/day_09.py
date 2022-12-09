from typing import Tuple

movement_map = dict(
    R=(0, 1),
    L=(0, -1),
    U=(-1, 0),
    D=(1, 0)
)

sign = lambda x: x and (1, -1)[x < 0]


def move(data: str, n_knots=2):
    knots = [(0, 0) for x in range(n_knots)]
    positions = []
    lines = data.split('\n')
    for line in lines:
        d, n = line.split(' ')
        n = int(n)
        for i in range(n):
            H = knots[0]
            knots[0] = tuple(map(sum, zip(H, movement_map[d])))
            for k in range(1, len(knots)):
                a = knots[k-1]
                b = knots[k]
                direction = follow(a, b)
                b = tuple(map(sum, zip(b, direction)))
                if k == n_knots - 1:
                    positions.append(b)
                knots[k-1] = a
                knots[k] = b
    return len(set(positions))


def dist_too_large(a: Tuple, b: Tuple):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** (1 / 2) >= 2


def follow(a: Tuple, b: Tuple):
    if dist_too_large(a, b):
        return sign(a[0] - b[0]), sign(a[1] - b[1])
    else:
        return 0, 0
