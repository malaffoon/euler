"""Problem 2 - Project Euler

Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:
  1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.

Optimization
 * both approaches are pretty damn fast
"""
import itertools as it
from utils.fibonacci import fibgen


class Problem2(object):
    @staticmethod
    def solve_simple(max_value=4000000):
        # NOTE: even though the sequence is defined differently ([1,1,2,3,...] vs. [1,2,3...])
        # i'm not correcting for it because it won't affect the result.
        return sum(filter(lambda n: n % 2 == 0, fibgen(max_value=max_value, max_count=None)))

    @staticmethod
    def solve(max_value=4000000):
        # since we know every 3rd fibonacci is even, just sum those ...
        return sum(it.islice(fibgen(max_value=max_value, max_count=None), 2, None, 3))

    @staticmethod
    def get_tests():
        return [(4000000, 4613732), (100, 44)]


if __name__ == '__main__':
    print("The sum of the even-valued Fibonacci numbers that don't exceed 4000000 is", Problem2().solve(4000000))
