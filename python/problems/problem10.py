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

    @staticmethod
    def get_tests():
        return [(2000000, 142913828922), (10, 17)]


if __name__ == '__main__':
    print("The sum of all the primes below two million is", Problem10().solve())
