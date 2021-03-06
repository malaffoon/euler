""" Problem 20 - Project Euler

Factorial digit sum

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

import math


class Problem20(object):
    @staticmethod
    def solve(n=100):
        return sum(int(c) for c in str(math.factorial(n)))

    @staticmethod
    def get_tests():
        return [(100, 648), (10, 27)]


if __name__ == '__main__':
    print("The sum of the digits in the number 100! is", Problem20().solve())