"""Helpers for dealing with prime numbers
"""

import functools
import itertools
import threading
from math import ceil, log, sqrt


__sieve_lock__ = threading.Lock()
__sieve__ = [False, False, True, True, False, True, False, True, False, False, False]


def __ensure_sieve__(limit):
    global __sieve__
    global __sieve_lock__
    if len(__sieve__) < limit:
        with __sieve_lock__:
            if len(__sieve__) < limit:
                __sieve__.extend([True] * (limit - len(__sieve__)))
                for (i, flag) in enumerate(__sieve__):
                    if flag:
                        for n in range(i*i, limit, i):
                            __sieve__[n] = False
    return __sieve__


def prime_factors(value):
    return list(factors(value))


def factors(value):
    """A generator for the prime factors of a value"""
    if value <= 3:
        yield int(value)
        return
    # loop this way to avoid calculating all the primes up to sqrt if not necessary
    for prime in primes(ceil(sqrt(value))):
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
    return itertools.islice(primes(guess_limit(n)), n - 1, n).__next__()


def primes(limit):
    """Generate primes less than limit"""
    for (i, flag) in enumerate(__ensure_sieve__(limit)[:limit]):
        if flag: yield i


def is_prime(value):
    """Return true if value is prime

    A previous implementation used the sieve to determine primality. Something like:
      | return __ensure_sieve__(value + 1)[value]
    That was very fast once the sieve was populated. But it requires the sieve
    to be calculated up to the value which can be both big and slow. The current
    algorithms trades off repeat performance for lower overhead.
    """
    if value <= 1: return False
    if value < len(__sieve__): return __sieve__[value]
    return all(value % p != 0 for p in primes(1 + ceil(sqrt(value))))


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