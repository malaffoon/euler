"""Helpers for dealing with prime numbers

TODO - consider Sieve of Atkin or other modern improvement
"""

import functools
import itertools
import operator
import threading
from math import ceil, log, sqrt

import collections

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
                        for n in range(i * i, limit, i):
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
    for prime in primes(int(1 + sqrt(value))):
        while value > 1 and value % prime == 0:
            yield prime
            value //= prime
        if value == 1 or value <= prime * prime:
            break
    if value > 1:
        yield value


def factors_grouped(value):
    """Returns a list of tuples with each unique prime factor and its exponent, for example:

      | factors(50) = (2, 5, 5)
      | factors_grouped(50) = [(2, 1), (5, 2)]
    Groups are sorted ascending by factor.
    """
    return sorted(list(collections.Counter(factors(value)).items()), key=lambda t: t[0])


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

    Note: returns false for 0 and 1
    """

    if value <= 1: return False
    # use existing sieve values for quick answer
    if value < len(__sieve__): return __sieve__[value]

    # There have been a few iterations of this method.
    #
    # First one simply used the sieve calculated to the value, something like:
    #   return __ensure_sieve__(value + 1)[value]
    #
    # Next it used the sieve is already calculated but avoided taking the big hit
    # of calculating the sieve all the way up to the number by dividing up to sqrt:
    #   return all(value % p != 0 for p in primes(1 + ceil(sqrt(value))))
    #
    # Still too slow, so time for Miller-Rabin
    return _MillerRabin(value)


# for small n, we can limit the a's to test (https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)
_test_limits = [
    (1373653, (2, 3)),
    (9080191, (31, 73)),
    (25326001, (2, 3, 5)),
    (3215031751, (2, 3, 5, 7)),
    (4759123141, (2, 7, 61)),
    (2152302898747, (2, 3, 5, 7, 11)),
    (3474749660383, (2, 3, 5, 7, 11, 13)),
    (341550071728321, (2, 3, 5, 7, 11, 13, 17))
]


def _MillerRabin(n, _precision_for_large_n=16):
    if n in _known_primes: return True
    if any((n % p) == 0 for p in _known_primes): return False

    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1

    def _try_composite(a, d, n, s):
        if pow(a, d, n) == 1: return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1: return False
        return True

    for tl in _test_limits:
        if n < tl[0]: return not any(_try_composite(a, d, n, s) for a in tl[1])
    return not any(_try_composite(a, d, n, s) for a in _known_primes[:_precision_for_large_n])


_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if _MillerRabin(x)]


def divisors(value):
    """Return a list of the divisors of a value. Always includes 1 and the value

        divisors(12) = [1, 2, 3, 4, 6, 12]
    """

    def prod(values):
        return functools.reduce(lambda x, y: x * y, values, 1)

    # have to get primes as list so it can be reused in loop
    plist = list(factors(value))

    # run through set to dedup
    result = list(set(prod(combo) for combo in itertools.chain.from_iterable(
        itertools.combinations(plist, l) for l in range(1, len(plist) + 1))))
    result.append(1)
    result.sort()
    return result


def phi(n):
    """Euler's Totient function, phi(n) returns the number of numbers that are less than
    n which are relatively prime to n. For example, 1, 2, 4, 5, 7, 8 are less than 9 and
    relatively prime to 9 so phi(9) = 6. For any prime number all numbers less than n are
    relatively prime so phi(p) = p - 1.

    This relies on a formula from the interwebs:
      | φ(n) = n∏(1-1/p) where the product is over the distinct prime numbers dividing n
    """
    return int(functools.reduce(operator.mul, map(lambda p: 1 - 1 / p, set(factors(n))), n))
