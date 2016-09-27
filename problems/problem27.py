"""Problem 27 - Project Euler

Quadratic primes

Euler discovered the remarkable quadratic formula:
    n^2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when
n=40,40^2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,41^2+41+41 is clearly divisible by 41.

The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the consecutive
values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:
    n^2+an+b, where |a|<1000|a|<1000

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number
of primes for consecutive values of n, starting with n==0.

I made some simplifying observations that significantly sped this up.
i. prime numbers must be positive
1. since n=0 must produce a prime then b must be prime and > 1
2. if a is even then n(a+n) will be odd/even based on n; an odd result + b will be even which is not prime;
so a must be odd
3. since n=1 must produce a prime then a > -b
...
all this makes me think there might be a non-algorithmic way to solve this
"""

import itertools
from utils.prime import primes, is_prime


class Problem27(object):
    @staticmethod
    def solve():
        max_primes = 0
        result = None
        for b in primes(1001):
            for a in range(-b, 1000, 2):
                n = Problem27.number_of_primes_for(a, b)
                if n > max_primes:
                    result = a * b
                    max_primes = n
        return result

    @staticmethod
    def number_of_primes_for(a, b):
        def quad(n): return n * n + a * n + b
        return sum(1 for _ in itertools.takewhile(lambda x: x > 1 and is_prime(x), (quad(n) for n in itertools.count())))


if __name__ == '__main__':
    print("The answer is", Problem27.solve())
