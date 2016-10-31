"""Problem 63 - Project Euler

Powerful digit counts

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

Algorithm. I suppose i could just let the computer count things but ...
  | n is the power/exponent
  | x is the base
  | 10^(n-1) <= x^n < 10^n
  | => 10^((n-1)/n) <= x < 10
  | => 1 <= n < 22
So, just count 'em
"""
import math


class Problem63(object):
    @staticmethod
    def solve():
        return sum(10 - math.ceil(10**((n-1)/n)) for n in range(1, 22))

    @staticmethod
    def get_tests():
        return [(None, 49)]


if __name__ == '__main__':
    print("The answer is", Problem63.solve())
