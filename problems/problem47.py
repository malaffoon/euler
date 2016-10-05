"""Problem 47 - Project Euler

Distinct primes factors

The first two consecutive numbers to have two distinct prime factors are:
  | 14 = 2 × 7
  | 15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:
  | 644 = 2² × 7 × 23
  | 645 = 3 × 5 × 43
  | 646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors.
What is the first of these numbers?
"""
from itertools import count

from utils.iter import slide
from utils.prime import factors


class Problem47(object):
    @staticmethod
    def solve(distinct=4):
        return Problem47.solve_sieve(distinct)

    @staticmethod
    def solve_sieve(distinct=4):
        # 140ms
        # create the sieve of distinct prime counts
        limit = 150000
        sieve = [0] * limit
        sieve[0] = sieve[1] = None
        for (i, d) in enumerate(sieve):
            if d == 0:
                for n in range(i, limit, i):
                    sieve[n] += 1
        # find consecutive numbers with matching distinct count
        for (i, w) in enumerate(slide(sieve, distinct)):
            if all(d == distinct for d in w):
                return i

    @staticmethod
    def solve_brute(distinct=4):
        # 3.6s
        for (i, w) in enumerate(slide(count(), distinct)):
            if all(len(set(factors(d))) == distinct for d in w):
                return i


if __name__ == '__main__':
    print("The answer is", Problem47.solve())
