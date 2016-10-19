"""Problem 53 - Project Euler

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,
nCr = n! / r!(n−r)!
where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?

Optimizations:
 * nCr == nC(n-r) so we only have to go halfway with r and then double it (give or take)
 * nC1 == nC(n-1) == n so we can skip that for n <= 1000000
 * nC2 == nC(n-2) == n(n-1) so we can skip that for n <= 1000
 * so, r goes from 3 to n//2
Alternate approach
 * as soon as we hit an r where nCr > 1000000
    * increment count by
"""
import math


class Problem53(object):
    @staticmethod
    def solve():
        count = 0
        for n in range(10, 101):
            for r in range(3, n//2 + 1):
                if math.factorial(n) / math.factorial(r) / math.factorial(n-r) > 1000000:
                    if n % 2 == 0:  # e.g. 24C9 -> 7 (9,10,11,12,13,14,15)
                        count += 2 * (n//2 - r) + 1
                    else:           # e.g. 23C10 -> 4 (10,11,12,13)
                        count += 2 * (n//2 - r + 1)
                    break
        return count

    @staticmethod
    def get_tests():
        return [(None, 4075)]


if __name__ == '__main__':
    print("The answer is", Problem53.solve())
