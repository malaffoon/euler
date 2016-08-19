"""Problem 5 - Project Euler

   Smallest multiple

   2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

   What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from functools import reduce
from math import gcd


class Problem5(object):
    @staticmethod
    def solve():
        return least_common_multiple(range(1,20))


def least_common_multiple(values):
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, values, 1)


if __name__ == '__main__':
    print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is", Problem5().solve())
