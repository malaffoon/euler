""" Problem 21 - Project Euler

Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from utils.prime import divisors


class Problem21(object):
    @staticmethod
    def solve():
        return sum(n for n in range(1, 10000) if is_amicable_number(n))


def is_amicable_number(n):
    s = sum(proper_divisors(n))
    return s != n and n == sum(proper_divisors(s))


def proper_divisors(n):
    """Proper divisors do not include the number itself"""
    return divisors(n)[0:-1]


if __name__ == '__main__':
    print("The sum of all the amicable numbers under 10000 is", Problem21().solve())