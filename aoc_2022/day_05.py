import re
from typing import Iterator, List, Tuple


def parse(input: str) -> Tuple[Iterator, List]:
    stack, plan = input.split('\n\n')

    stack_list = {}
    length = 1
    j = 0
    for i, x in enumerate(stack):
        if re.match(r'\d', x):
            break
        if j == 0:
            j += 1
            continue
        stack_num = ((j - 1) // 4)
        if ((j - 1) % 4 == 0 or j == 1) and re.match(r'\w', x):
            stack_list.setdefault(stack_num, []).append(x)
        if re.match('\n', x):
            j = 0
            continue
        j += 1
    stack_list = [stack_list[k] for k in range(len(stack_list))]
    stack_list = map(list, map(reversed, stack_list))

    moves = [re.findall(r'\d+', line) for line in plan.split('\n')]
    moves = [[int(x) for x in y] for y in moves]

    return list(stack_list), moves


def move(stack_list: List[List], moves: List, multiple=False):
    for n, x, y in moves:
        if multiple:
            stack_list[y-1].extend(stack_list[x-1][-n:])
            del stack_list[x-1][-n:]
        else:
            for i in range(n):
                stack_list[y - 1].append(stack_list[x - 1].pop())
    return stack_list


def get_tops(stack_list):
    return ''.join([x.pop() for x in stack_list])
