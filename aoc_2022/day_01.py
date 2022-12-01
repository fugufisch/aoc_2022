from typing import List


def top_calories(parsed_input: List[List[str]], n=3):
    return sorted(map(sum, parsed_input), reverse=True)[0:n]


def parse_calories(raw_input: str) -> List[List[str]]:
    buckets = [map(int, bucket.split('\n')) for bucket in raw_input.split('\n\n')]
    return buckets
