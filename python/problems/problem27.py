"""Problem 27 - Project Euler

Quadratic primes

Euler discovered the remarkable quadratic formula:
    n^2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when
n=40,40^2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,41^2+41+41 is clearly divisible by 41.

The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the consecutive
values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:
    n^2+an+b, where |a|<1000 and |b|<=1000

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

After brute forcing the answer, i read the forum. Somebody did work through the algebra:
They noted that n^2-79n+1601 = (n-40)^2+n-40+41, i.e. p^2+p+41 where p=n-40
They surmised that the best solution will have the same form, i.e. (n-x)^2+n-x+41
Doing maths, (n-x)^2+n-x+41 = n^2+(1-2x)n+x^2-x+41 = n^2+an+b, a=1-2x, b=x^2-x+41.
Applying the range limits to b, basically solving x^2-x+41=1000, gives x~31.
Plug that back in gives a=-61, b=971. Which is the solution, ab=-59231.
"""

import itertools
from utils.prime import primes, is_prime


class Problem27(object):
    @staticmethod
    def solve():
        a, b = -61, 971
        return a * b

    @staticmethod
    def brute_force():
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
    def get_tests():
        return [(None, -59231)]

    @staticmethod
    def number_of_primes_for(a, b):
        def quad(n): return n * n + a * n + b
        return sum(1 for _ in itertools.takewhile(lambda x: x > 1 and is_prime(x), (quad(n) for n in itertools.count())))


if __name__ == '__main__':
    print("The answer is", Problem27.solve())
