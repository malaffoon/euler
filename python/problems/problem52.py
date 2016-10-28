"""Problem 52 - Project Euler

Permuted multiples

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits,
but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""
import itertools as it

class Problem52(object):
    @staticmethod
    def solve(N=6):
        def equivalent(first, values):
            first.sort()
            for value in values:
                v = list(d for d in str(value))
                if len(first) != len(v): return False
                v.sort()
                if first != v: return False
            return True

        for i in it.count(100000):
            first = list(d for d in str(i))
            if N >=5 and '5' not in first: continue
            if equivalent(first, [n*i for n in range(2, N+1)]):
                return i

    @staticmethod
    def get_tests():
        return [(None, 142857), (2, 125874)]


if __name__ == '__main__':
    print("The answer is", Problem52.solve())
