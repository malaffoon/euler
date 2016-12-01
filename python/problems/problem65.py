"""Problem 65 - Project Euler

Convergents of e

(the continued fraction stuff)
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...]
"""

import itertools as it

from utils.continued_fraction import ContinuedFraction


class Problem65(object):
    @staticmethod
    def solve(n=100):
        # get nth convergent but all that is needed is sum of digits of the numerator
        h, k = next(it.islice(ContinuedFraction.for_e(n).convergents(), n-1, n))
        return sum(int(d) for d in str(h))

    @staticmethod
    def get_tests():
        return [(100, 272), (10, 17)]


if __name__ == '__main__':
    print("The answer is", Problem65.solve())
