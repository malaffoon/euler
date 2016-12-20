"""Problem 69 - Project Euler

Totient maximum

Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number
of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are
all less than nine and relatively prime to nine, φ(9)=6.

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10, 3.0.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

Optimization
FYI, brute force looping through all n ≤ 1,000,000 did work in less than a minute, but just barely.

For prime n, φ(n) = n - 1, and n/φ(n) ~ 1
φ(n) will be smallest when n is a product of unique primes because that eliminates the most numbers without redundancy.
So, can we just calculate the largest product of unique primes that is less than a million?
"""
from math import sqrt

from utils.prime import primes


class Problem69(object):
    @staticmethod
    def solve(N=1000000):
        prod = 1
        for p in primes(int(1 + sqrt(N))):
            if prod * p > N: break
            prod *= p
        return prod

    @staticmethod
    def get_tests():
        return [(None, 510510), (10, 6)]


if __name__ == '__main__':
    print("The answer is", Problem69.solve())
