"""Problem 64 - Project Euler

Odd period square roots
"""
import math


class Problem64(object):
    @staticmethod
    def solve(n=10000):
        def helper(n):
            """Calculate the continued fraction for the square root of any natural number.

            Returns a tuple of (int, (loop))

            m(0) = 0, d(0) = 1, a(0) = int(sqrt(n))
            for x+1:
            m(x+1) = d(x)a(x) - m(x)
            d(x+1) = (S - m(x+1)^2) / d(x)
            a(x+1) = int((a(0) + m(x+1))/d(x+1))

            stop when a(x+1) = 2 * a(0)

            Taken from https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
            """

            a0 = int(math.sqrt(n))
            if a0 * a0 == n:
                return a0, ()
            a, m, d = a0, 0, 1
            loop = []
            while a != (2*a0):
                m = d * a - m
                d = (n - m*m) / d
                a = int((a0 + m)/d)
                loop.append(a)
            return a0, tuple(loop)

        return sum(map(lambda x: len(helper(x)[1]) % 2, range(n + 1)))

    @staticmethod
    def get_tests():
        return [(None, 1322), (13, 4)]


if __name__ == '__main__':
    print("The answer is", Problem64.solve())
