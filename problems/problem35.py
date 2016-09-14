"""Problem 35 - Project Euler

Circular primes

The number 197 is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from utils.prime import is_prime, generator


class Problem35(object):
    @staticmethod
    def solve(limit=1000000):
        return sum(1 for n in generator(limit) if is_circular_prime(n))


def is_circular_prime(n):
    if n < 10:
        # single digits are always circular
        return True
    s = str(n)
    if any(d in s for d in '024568'):
        # evens and five's can't be prime
        return False
    for i in range(1, len(s)):
        s = s[1:] + s[:1]
        if not is_prime(int(s)):
            return False
    return True


if __name__ == '__main__':
    print("The number of circular primes below one million is", Problem35.solve())
