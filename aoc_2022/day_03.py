import string
from typing import Iterator


def get_sum(data: str, part=1):
    rucksacks = data.split('\n')
    order = string.ascii_lowercase + string.ascii_uppercase
    if part == 1:
        items = [get_non_unique(rucksack) for rucksack in rucksacks]
    else:
        items = [get_intersection(rucksacks[x:x + 3]) for x in range(0, len(rucksacks), 3)]
    return sum([order.index(x) + 1 for x in items])


def get_non_unique(rucksack: str):
    size = len(rucksack)
    compartment_1, compartment_2 = rucksack[0:size // 2], rucksack[size // 2:size]
    intersection = set(compartment_1).intersection(compartment_2)
    return intersection.pop()


def get_intersection(rucksacks: Iterator):
    return set.intersection(*[set(x) for x in rucksacks]).pop()
