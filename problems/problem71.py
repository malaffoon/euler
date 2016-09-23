"""Problem 71 - Project Euler

Ordered fractions

Consider the fraction, n/d, where n and d are positive integers.
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size,
find the numerator of the fraction immediately to the left of 3/7.
"""

from math import floor, gcd


class Problem71(object):
    @staticmethod
    def solve(maxD=1000000, right=3/7):
        # 350ms
        # generating iterables of tuples, e.g. (n,d) or (diff,(n,d)) hurt performance quite a bit (-> 1000ms)
        # using min(result, (diff, (n,d))) was slower (-> 600ms)
        result = (1.0, None)  # (diff,(n,d))
        for d in range(3, maxD+1):
            n = floor(right * d)
            diff = right - n/d
            if 0 < diff < result[0] and gcd(n, d) == 1:
                result = (diff, (n, d))
        return result[1][0]

    @staticmethod
    def solve_loop(maxD=8, right=3/7):
        # O(n**2) and for n=10000 -> 20s, so n=1000000 -> 60 hours
        result = (1.0, None)
        for f in ((n, d) for d in range(3, maxD + 1) for n in range(1, d) if n / d < right and gcd(n, d) == 1):
            result = min(result, (right - f[0] / f[1], f), key=lambda r: r[0])
        return result[1][0]

    @staticmethod
    def solve_list(maxD=8):
        # worse than O(n**2) and for n=10000 -> 45s, so n=1000000 -> 150 hours
        rpfs = [(n, d) for d in range(2, maxD + 1) for n in range(1, d) if gcd(n, d) == 1]
        rpfs.sort(key=lambda f: f[0] / f[1])
        return rpfs[rpfs.index((3, 7)) - 1][0]


if __name__ == '__main__':
    # answer is 428570/999997
    print("The answer is", Problem71.solve())
