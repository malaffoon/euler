""" Problem 24 - Project Euler

Lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the
digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import itertools


class Problem24(object):
    @staticmethod
    def solve(digits=range(0, 10), n=1000000):
        return ''.join(str(d) for d in itertools.islice(itertools.permutations(digits), n - 1, n).__next__())

    @staticmethod
    def get_tests():
        return [(None, '2783915460')]


if __name__ == '__main__':
    print("The millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9 is", Problem24.solve())