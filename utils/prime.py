"""Helpers for dealing with prime numbers
"""

import functools
import itertools
import threading
from math import ceil, log, sqrt


sieve_lock = threading.Lock()
sieve = [False, False, True, True]
def ensure_sieve(limit):
    if len(sieve) < limit:
        with sieve_lock:
            sieve.extend([True] * (limit-len(sieve)))
            for (i, flag) in enumerate(sieve):
                if flag:
                    for n in range(i*i, limit, i):
                        sieve[n] = False
    return sieve


def prime_factors(value):
    return list(factors(value))


def factors(value):
    """A generator for the prime factors of a value"""
    if value <= 3:
        yield int(value)
        return
    # loop this way to avoid calculating all the primes up to sqrt if not necessary
    for prime in generator(ceil(sqrt(value))):
        while value > 1 and value % prime == 0:
            yield prime
            value /= prime
        if value == 1:
            break
    if value > 1:
        yield int(value)


def nth(n):
    """Return the nth prime. Primes are 2, 3, 5, ... so

       * prime.nth(6) = 13
       * prime.nth(10) = 29
       * prime.nth(1000) = 7919
    """
    def guess_limit(n):
        return 30 if n < 10 else ceil(n * (log(n) + log(log(n))))
    return itertools.islice(generator(guess_limit(n)), n - 1, None).__next__()


def generator(limit):
    """Generate primes less than limit"""
    for (i, flag) in enumerate(ensure_sieve(limit)[:limit]):
        if flag: yield i


def is_prime(value):
    """Return true if value is prime"""
    return ensure_sieve(value+1)[value]


def divisors(value):
    """Return a list of the divisors of a value. Always includes 1 and the value

        divisors(12) = [1, 2, 3, 4, 6, 12]
    """

    def prod(values):
        return functools.reduce(lambda x,y: x*y, values, 1)

    # have to get primes as list so it can be reused in loop
    plist = list(factors(value))

    # run through set to dedup
    result = list(set(prod(combo) for combo in itertools.chain.from_iterable(itertools.combinations(plist, l) for l in range(1, len(plist)+1))))
    result.append(1)
    result.sort()
    return result