"""Problem 64 - Project Euler

Odd period square roots
"""
import math

from utils.continued_fraction import ContinuedFraction


class Problem64(object):
    @staticmethod
    def solve(n=10000):
        # for all values up to n
        #   get the continued fraction
        #   if length of terms is odd, count it
        return sum(map(lambda x: len(ContinuedFraction.forSqrtOf(x).terms) % 2, range(2, n + 1)))

    @staticmethod
    def get_tests():
        return [(None, 1322), (13, 4)]


if __name__ == '__main__':
    print("The answer is", Problem64.solve())
