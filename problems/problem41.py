"""Problem 41 - Project Euler

Pandigital prime

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

Optimization:
Pandigital numbers of length 2, 3, 5, 6, 8, and 9 will always be divisible by 3.
So skip up to 1,000,000, and stop at 10,000,000.
"""

from itertools import dropwhile

from utils.mathex import is_pandigital
from utils.prime import generator


class Problem41(object):
    @staticmethod
    def solve():
        return max(p for p in dropwhile(lambda x: x < 1000000, generator(10000000)) if is_pandigital(p))


if __name__ == '__main__':
    print("The answer is", Problem41.solve())
