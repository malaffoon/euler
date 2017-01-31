"""Problem 80 - Project Euler

Square root digital expansion

It is well known that if the square root of a natural number is not an integer, then it is irrational.
The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers,
find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.

NOTE: "the first one hundred decimal digits" includes the unit value (left of decimal) - stupid wording
So we need first digit, skip the decimal, and the next 99 digits; calculate extra digits to avoid rounding
"""
import decimal

from math import sqrt


class Problem80(object):
    @staticmethod
    def solve():
        decimal.getcontext().prec = 110
        result = 0
        for n in filter(lambda x: not sqrt(x).is_integer(), range(1, 101)):
            s = format(decimal.Decimal(n).sqrt(), '.110f')
            result += sum(int(d) for d in s[0] + s[2:101])
        return result

    @staticmethod
    def get_tests():
        return [(None, 40886)]


if __name__ == '__main__':
    print("The answer is", Problem80.solve())
