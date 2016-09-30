"""More math utils
"""

from functools import reduce
from itertools import count
from math import gcd


def lcm(values):
    """Return the Least Common Multiple of an iterable of values

       The LCM is the smallest number that is evenly divisible by all the values.
         lcm([8, 9, 12]) = 72
    """
    def lcm_pair(a, b):
        return a * (b // gcd(a, b))
    return reduce(lcm_pair, values, 1)


def champernowne():
    """A generator for the digits of champernowne's constant.

    Champernowne's constant is a number constructed by concatenating representations of successive integers.
    For example, in base 10:
      | 0.123456789101112131415...

    This infinite generator emits just the digits of the sequence, starting with 1.
    """
    for v in count(1):
        for d in str(v):
            yield int(d)


def digits(n):
    """returns digits of n in reverse order, faster than int(d)/str(n) approach

    Note: if performance is critical, it is better to inline this functionality than to call this generator.
    """
    while n:
        yield n % 10
        n //= 10


def is_pandigital(s):
    s = str(s)
    return all(str(n+1) in s for n in range(0, len(s)))
