"""Problem 41 - Project Euler

Pandigital prime

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from utils.mathex import is_pandigital
from utils.prime import generator


class Problem41(object):
    @staticmethod
    def solve():
        # NOTE: this isn't really a robust solution since i limit it to seven digits.
        # More than that took too long to solve, so i lucked out this was an okay limit.
        return max(p for p in generator(10000000) if is_pandigital(p))


if __name__ == '__main__':
    print("The answer is", Problem41.solve())
