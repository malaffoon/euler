"""Helpers for dealing with prime numbers
"""

from itertools import islice
from math import ceil, log, sqrt


def prime_factors(value):
    """Return a list of the prime factors of the value
       If the value is prime, a list of the single value will be returned
    """
    if value <= 3:
        return [value]

    factors = []

    # loop this way to avoid calculating all the primes up to sqrt if not necessary
    for prime in generator(ceil(sqrt(value))):
        while value > 1 and value % prime == 0:
            factors.append(prime)
            value /= prime
        if value == 1:
            break
    if value > 1:
        factors.append(value)

    return factors


def nth(n):
    """Return the nth prime. Primes are 2, 3, 5, ... so

       * prime.nth(6) = 13
       * prime.nth(10) = 29
       * prime.nth(1000) = 7919
    """
    def guess_limit(n):
        return 30 if n < 10 else ceil(n * (log(n) + log(log(n))))
    return islice(generator(guess_limit(n)), n - 1, None).__next__()


def generator(limit):
    """Generate primes less than limit"""
    e = [True] * limit
    e[0] = e[1] = False
    for (i, flag) in enumerate(e):
        if flag:
            yield i
            for n in range(i*i, limit, i):
                e[n] = False
