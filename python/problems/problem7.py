"""Problem 7 - Project Euler

10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

from utils import prime


class Problem7(object):
    @staticmethod
    def solve(value=10001):
        return prime.nth(value)

    @staticmethod
    def get_tests():
        return [(10001, 104743), (6, 13), (1, 2), (10, 29), (100, 541), (1000, 7919)]


if __name__ == '__main__':
    print("The 10001st prime number is", Problem7().solve())
