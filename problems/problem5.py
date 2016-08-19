"""Problem 5 - Project Euler

   Smallest multiple

   2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

   What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import functools
import operator

from utils.prime import primegen


class Problem5(object):
    @staticmethod
    def solve():
        return least_common_multiple(range(1,20))


def least_common_multiple(values):
    """Return least common multiple of given values"""
    if len(values) == 0: return 0
    if len(values) == 1: return values[0]
    if max(values) == 1: return 1

    values = list(values)
    factors = []
    for prime in primegen(1+max(values)):
        if max(values) == 1:
            break
        while True:
            factor = False
            for (v, value) in enumerate(values):
                if value % prime == 0:
                    values[v] = int(value/prime)
                    factor = True
            if factor: factors.append(prime)
            else: break
    return functools.reduce(operator.mul, factors, 1)


if __name__ == '__main__':
    print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is", Problem5().solve())
