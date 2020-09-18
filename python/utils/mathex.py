"""More math utils
"""

from functools import reduce
from itertools import count
from math import gcd, sqrt

from operator import mul


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


def prod(sequence):
    """return the product of values from a sequence

    Multiplication equivalent to sum()
    """
    return reduce(mul, sequence)


def is_pandigital(s):
    s = str(s)
    return all(str(n + 1) in s for n in range(0, len(s)))


def trigonal(n):
    return n * (n + 1) // 2


def is_trigonal(v):
    n = (sqrt(1 + 8 * v) - 1) / 2
    return int(n) if n.is_integer() else None


def tetragonal(n):
    return n * n


def is_tetragonal(v):
    n = sqrt(v)
    return int(n) if n.is_integer() else None


def pentagonal(n):
    return n * (3 * n - 1) // 2


def is_pentagonal(v):
    n = (sqrt(1 + 24 * v) + 1) / 6
    return int(n) if n.is_integer() else None


def hexagonal(n):
    return n * (2 * n - 1)


def is_hexagonal(v):
    n = (sqrt(1 + 8 * v) + 1) / 4
    return int(n) if n.is_integer() else None


def heptagonal(n):
    return n * (5 * n - 3) // 2


def is_heptagonal(v):
    n = (sqrt(9 + 40 * v) + 3) / 10
    return int(n) if n.is_integer() else None


def octagonal(n):
    return n * (3 * n - 2)


def is_octagonal(v):
    n = (sqrt(4 + 12 * v) + 2) / 6
    return int(n) if n.is_integer() else None


def isqrt(n):
    """An integer sqrt function for use before python 3.8 which has it builtin.
    NOTE: this returns the largest integer that is less than or equal to the
    square root. You must check the return value to see if it is exactly the
    square root.
    """
    if n > 0:
        x = 1 << (n.bit_length() + 1 >> 1)
        while True:
            y = (x + n // x) >> 1
            if y >= x:
                return x
            x = y
    elif n == 0:
        return 0
    else:
        raise ValueError("square root not defined for negative numbers")


_pell_smallest = (None,
                  None, (3, 2), (2, 1), None, (9, 4), (5, 2), (8, 3), (3, 1), None, (19, 6),
                  (10, 3), (7, 2), (649, 180), (15, 4), (4, 1), None, (33, 8), (17, 4), (170, 39), (9, 2)
                  )


def pell_gen(n: int) -> (int, int):
    """A generator for infinite sequences generated from the solutions to Pell's equation
    for the given n. Please see https://en.wikipedia.org/wiki/Pell%27s_equation.

    This only works for Pell's equation with a known fundamental solution for n.
    Obviously, you can expand the list by transcribing values from wikipedia.

    Note that the degenerate solution (1,0) is not returned.
    """
    if n > len(_pell_smallest) or _pell_smallest[n] is None:
        raise ValueError("Pell sequence unknown for n=" + str(n))
    x1, y1 = _pell_smallest[n]
    yield x1, y1
    x, y = x1, y1
    while True:
        curx = x
        x = x1 * x + n * y1 * y
        y = x1 * y + y1 * curx
        yield x, y