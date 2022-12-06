import re
from typing import List, Tuple


def parse(data):
    pairs = [re.match(r'(\d+)-(\d+),(\d+)-(\d+)', line).groups() for line in data.split('\n')]
    return pairs


def find_contained(pairs: List[Tuple], with_overlap=False):
    contained_list = []
    for pair in pairs:
        start1, end1, start2, end2 = (int(x) for x in pair)
        contained = (start1 >= start2 and end1 <= end2) or (start1 <= start2 and end1 >= end2)
        if with_overlap:
            overlap = start1 <= end2 and start2 <= end1
        else:
            overlap = False
        contained_list.append(contained or overlap)
    return sum(contained_list)
