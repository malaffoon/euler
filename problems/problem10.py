"""Problem 10 - Project Euler

Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from utils.prime import primes


class Problem10(object):
    @staticmethod
    def solve(limit=2000000):
        return sum(primes(limit))


if __name__ == '__main__':
    print("The sum of all the primes below ten is", Problem10().solve(10))
    print("The sum of all the primes below two million is", Problem10().solve())
