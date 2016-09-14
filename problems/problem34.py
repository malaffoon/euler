"""Problem 34 - Project Euler

Digit factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

NOTE: algorithmically very similar to Problem 30
"""


class Problem34(object):
    @staticmethod
    def solve(limit=None):
        def is_curious(n):
            return n == sum(Problem34.__factorials__[d] for d in str(n))

        return sum(n for n in range(10, limit if limit else Problem34.__max_limit__) if is_curious(n))

    """precomputed lookup table for factorials, and max limit for this problem"""
    __factorials__ = {'0': 1, '1': 1, '2': 2, '3': 6, '4': 24, '5': 120, '6': 720, '7': 5040, '8': 40320, '9': 362880}
    __max_limit__ = 7 * __factorials__['9']


if __name__ == '__main__':
    print("The answer is", Problem34.solve())
