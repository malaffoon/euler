"""More math utils
"""

from functools import reduce
from math import gcd


def lcm(values):
    """Return the Least Common Multiple of an iterable of values

       The LCM is the smallest number that is evenly divisible by all the values.
         lcm([8, 9, 12]) = 72
    """
    def lcm_pair(a, b):
        return a * (b // gcd(a, b))
    return reduce(lcm_pair, values, 1)
