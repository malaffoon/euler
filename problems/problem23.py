""" Problem 23 - Project Euler

Non-abundant sums

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from utils.prime import divisors


class Problem23(object):
    @staticmethod
    def solve():
        def is_abundant(n):
            return sum(divisors(n)[:-1]) > n

        # create a sieve: mark all values that are summable, then sum up remaining False entries
        summable = [False] * 28124
        abundants = [n for n in range(1, 28124) if is_abundant(n) > 0]
        for i in range(0, len(abundants)):
            for j in range(i, len(abundants)):
                s = abundants[i] + abundants[j]
                if s >= len(summable):
                    break
                summable[s] = True
        return sum(i for i, flag in enumerate(summable) if not flag)


if __name__ == '__main__':
    print("The sum of all the positive integers which cannot be written as the sum of two abundant numbers is", Problem23.solve())