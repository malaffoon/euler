"""Problem 40 - Project Euler

Champernowne's constant

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000


Lesson Learned:
1. islice is 300x faster compared to manually advancing an iterator.

"""
from functools import reduce
from itertools import chain, count, islice, takewhile
from operator import mul

_positions = [1, 10, 100, 1000, 10000, 100000, 1000000]


class Problem40(object):
    @staticmethod
    def solve():
        # 0.09s
        return reduce(mul, (int(next(islice(chain.from_iterable(str(n) for n in count(1)), p - 1, None))) for p in _positions))

    @staticmethod
    def get_tests():
        return [(None, 210)]

    @staticmethod
    def solve3():
        # 0.17s
        def skip(it, n):
            for _ in range(0, n):
                it.__next__()

        it = chain.from_iterable(str(n) for n in count(1))
        product = 1
        for skips in [0, 8, 89, 899, 8999, 89999, 899999]:
            skip(it, skips)
            product *= int(next(it))
        return product

    @staticmethod
    def solve4():
        # 0.62s
        return reduce(mul,
                      map(lambda e: int(e[1]),
                          filter(lambda e: e[0] in _positions,
                                 takewhile(lambda e: e[0] <= _positions[-1],
                                           enumerate(chain.from_iterable(str(n) for n in count(1)), start=1)))))


if __name__ == '__main__':
    print("The answer is", Problem40.solve())
