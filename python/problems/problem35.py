"""Problem 35 - Project Euler

Circular primes

The number 197 is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
from utils.iter import rotations
from utils.prime import is_prime, primes


class Problem35(object):
    @staticmethod
    def solve(limit=1000000):
        def is_circular_prime(n):
            if n < 10:
                # single digits are always circular
                return True
            s = str(n)
            if any(d in s for d in '024568'):
                # evens and fives can't be prime
                return False
            return all(is_prime(v) for v in rotations(n))

        return sum(1 for n in primes(limit) if is_circular_prime(n))

    @staticmethod
    def get_tests():
        return [(1000000, 55), (100, 13)]


if __name__ == '__main__':
    print("The number of circular primes below one million is", Problem35.solve())
