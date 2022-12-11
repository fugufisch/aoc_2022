from functools import reduce
from math import gcd
from typing import List


class Monkey:
    def __init__(self, name, items: List[int], operation: str, test: str):
        self.inspection_count = 0
        self.name = name
        self._items = items
        self.operation = operation
        self.test, self.divisor = self.__parse_test(test)

    def __parse_test(self, test):
        divisor = int(test[0].lstrip('  Test: divisible by '))
        t = int(test[1].lstrip('    If true: throw to monkey '))
        f = int(test[2].lstrip('    If false: throw to monkey '))

        def test(x):
            return t if x % divisor == 0 else f

        return test, divisor

    def catch(self, item):
        self._items.append(item)

    def throw(self, super_worried=False, great_mod=0):
        old = self._items.pop(0)
        new = eval(self.operation)
        self.inspection_count += 1
        if not super_worried:
            new = new // 3
        else:
            new = new % great_mod
        return self.test(new), new

    def has_items(self):
        return len(self._items) > 0


class KeepAway:
    def __init__(self, setup_file, super_worried=False):
        self.monkeys = []
        self.super_worried = super_worried
        for monkey in setup_file.split('\n\n'):
            monkey_conf = monkey.split('\n')
            name = monkey_conf[0].strip(":")
            items = [int(x) for x in monkey_conf[1].lstrip("  Starting items: ").split(', ')]
            operation = monkey_conf[2].replace(r"  Operation: new = ", '')
            test = monkey_conf[3:]
            self.monkeys.append(Monkey(name, items, operation, test))
        self.great_mod = reduce(lambda a, b: a * b, [monkey.divisor for monkey in self.monkeys])

    def play_round(self):
        for monkey in self.monkeys:
            while monkey.has_items():
                target, item = monkey.throw(super_worried=self.super_worried,
                                            great_mod=self.great_mod)
                self.monkeys[target].catch(item)
