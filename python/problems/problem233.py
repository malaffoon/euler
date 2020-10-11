"""Problem 233 - Project Euler

Lattice points on a circle

Let f(N) be the number of points with integer coordinates that are on a circle
passing through (0,0), (N,0), (0,N), and (N,N).

It can be shown that f(10000) = 36.

What is the sum of all positive integers N ≤ 10^11 such that f(N) = 420 ?


--------------------------------------------------------------------------------------------------

Equation of circle is: (x - N/2)^2 + (y - N/2)^2 = N^2 / 2

https://en.wikipedia.org/wiki/Sum_of_squares_function
https://en.wikipedia.org/wiki/Sum_of_two_squares_theorem
http://mathworld.wolfram.com/CircleLatticePoints.html

Number theory says the number of integer solutions of x^2 + y^2 = k can be calculated.
Prime factorization, k = 2 x p1^f1 x p2^f2 x ... x q1^h1 x q2^h2 x ..., where p is 1mod4 and q is 3mod4.
Then r(k) = 4 x (f1+1) x (f2+1)...; if all h are even, else r(k) = 0.

We want r(k) = 420 -> (f1+1)x(f2+1)x(f3+1) = 105
There are only a few ways to do that: 3x5x7, 7x15, 5x21, 3x35, 105.
Combine p's with f's as (2,4,6),(6,14),(4,20),(2,34),(104).
Since the smallest p is 5, the last two combinations can be eliminated, 5^34 > 1e23.
And k ~ N*N, use square root, so we want p's with f's as (1,2,3),(3,7),(2,10).
And we can multiply by any number without a prime factor p until we hit N.

p's: 5,13,17,29,37,41,53,61,73,89,97,...
"""
from utils.prime import primes


class Problem233(object):
    @staticmethod
    def solve():
        maxN = 10**11

        # calculate "base" values, p1^f1 * p2^f2 * p3^f3, that are less than maxN
        # maxP is calculated knowing that p0=5, p1=13, p3=maxP for first set of f's
        maxP = int(maxN/5**3/13**2)
        ps = [p for p in primes(maxP) if p % 4 == 1]
        fs = [(3, 2, 1), (7, 3, 0), (10, 2, 0)]

        base_values = []
        for (f1, f2, f3) in fs:
            for p1 in ps:
                v1 = p1**f1
                if v1 > maxN:
                    break
                for p2 in (p for p in ps if p != p1):
                    v2 = v1 * p2**f2
                    if v2 > maxN:
                        break
                    if f3 == 0:
                        base_values.append(v2)
                    else:
                        for p3 in (p for p in ps if p != p1 and p != p2):
                            v3 = v2 * p3**f3
                            if v3 > maxN:
                                break
                            base_values.append(v3)

        # calculate all multiples of the base_values that don't exceed maxN
        # where the multiple doesn't have a 1mod4 prime factor in it
        # build list of factors by crossing out multiples of ps
        maxF = maxN // base_values[0] + 1
        sieve = [False] + [True] * maxF
        for p in ps:
            for f in range(p, maxF+1, p):
                sieve[f] = False
        factors = [f for f, flag in enumerate(sieve) if flag]

        sumN = 0
        for value in base_values:
            for f in factors:
                val = value * f
                if val > maxN: break
                sumN += val

        return sumN

    @staticmethod
    def get_tests():
        return [(None, 271204031455541309)]


if __name__ == '__main__':
    print("The answer is", Problem233.solve())
