"""Problem 77 - Project Euler

Prime summations

It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?

Same trick as 31, 76
"""

from utils import prime


class Problem77(object):
    @staticmethod
    def solve():
        # back of envelope shows it'll be less than 100
        n = 100
        primes = list(prime.primes(n))
        combos = [1, 0] + [0] * n
        for p in primes:
            for c in range(p, n+2):
                combos[c] += combos[c-p]
        return next(i for i, c in enumerate(combos) if c > 5000)

    @staticmethod
    def get_tests():
        return [(None, 71)]


if __name__ == '__main__':
    print("The answer is", Problem77.solve())
