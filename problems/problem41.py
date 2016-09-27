"""Problem 41 - Project Euler

Pandigital prime

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

Optimization:
Pandigital numbers of length 2, 3, 5, 6, 8, and 9 will always be divisible by 3.
"""

from itertools import dropwhile, permutations

from utils.mathex import is_pandigital
from utils.prime import primes, is_prime


class Problem41(object):
    @staticmethod
    def solve():
        return Problem41.solve_by_perms()

    @staticmethod
    def solve_by_perms():
        # takes 1ms first run, 0.4ms second run
        return next(n for n in (int(''.join(p)) for p in permutations('7654321', 7)) if is_prime(n))

    @staticmethod
    def solve_by_primes():
        # takes 3s first run, 1s second run
        return max(p for p in dropwhile(lambda x: x < 1234567, primes(7654322)) if is_pandigital(p))


if __name__ == '__main__':
    print("The answer is", Problem41.solve())
