"""Problem 70 - Project Euler

Totient permutation

Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive
numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all
less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.

Optimization
FYI, brute force worked but took many many minutes.

For prime n, φ(n) = n - 1, and n/φ(n) ~ 1 ; although ratio would be small the answer clearly won't be a prime.

To minimize the ratio, we want φ(n) to be as large as possible (while keeping n small if possible).
Looking on the interwebs:
  | φ(n) = n∏(1-1/p) where the product is over the distinct prime numbers dividing n, so
  | n/φ(n) = 1 / ∏(1-1/p)
So we want to maximize that product. Try expanding the product with some examples and you'll notice that
it gets smaller every time a prime is added, and the smaller the prime, the smaller it gets. So we want
n that is a product of two or more large primes.

So, get a list of primes that might produce a product less than N and try combinations of them.

Further, the calculation of φ(n) when you know the primes is much simpler:
  | φ(n) = n∏(1-1/p) = n(1-1/p1)(1-1/p2) = p1p2(1-1/p1)(1/1-p2) = (p1-1)(p2-1)
"""
from math import sqrt

import itertools

from utils.mathex import digits
from utils.prime import primes


class Problem70(object):
    @staticmethod
    def solve():
        def is_permutation(x, y):
            return sorted(digits(x)) == sorted(digits(y))

        N = 10000000
        lowerP = int(sqrt(N)/1.5)
        upperP = int(sqrt(N)*1.5)
        p = list(itertools.dropwhile(lambda x: x < lowerP, primes(upperP)))

        minN, minRatio = None, N
        for n, φ in ((p1*p2, (p1-1)*(p2-1)) for p1 in p for p2 in p):
            if n > N: continue
            if is_permutation(n, φ):
                ratio = n/φ
                if ratio < minRatio:
                    minN, minRatio = n, ratio
        return minN

    @staticmethod
    def get_tests():
        return [(None, 8319823)]


if __name__ == '__main__':
    print("The answer is", Problem70.solve())