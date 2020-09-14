"""Problem 78 - Project Euler

Coin partitions

Let p(n) represent the number of different ways in which n coins can be separated into piles.
For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO O
OOO OO
OOO O O
OO OO O
OO O O O
O O O O O

Find the least value of n for which p(n) is divisible by one million.

---------------------------------------------------------------------------------------------------
The number of partitions of n: https://oeis.org/A000041
1, 1, 2, 3, 5, 7, 11, 15, 22, 30, ...
calc_p and approx_p are derived from pseudo-code on that site.

Apparently sympy.ntheory.npartitions exists, could probably use that.

Turns out calc_p with memoization is fast enough; probably be faster with sympy or numba but ... meh
"""
import math


memo_p = {k: v for k, v in enumerate([1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56, 77, 101, 135, 176, 231, 297, 385, 490, 627, 792, 1002, 1255, 1575, 1958, 2436, 3010, 3718, 4565, 5604, 6842, 8349, 10143, 12310, 14883, 17977, 21637, 26015, 31185, 37338, 44583, 53174, 63261, 75175, 89134, 105558, 124754, 147273, 173525])}
def calc_p(n: int) -> int:
    if n in memo_p:
        return memo_p[n]
    j = n - 1
    k = 2
    s = 0
    while j >= 0:
        t = calc_p(j)
        s = s+t if (k//2) % 2 != 0 else s-t
        j = j - (k if k % 2 != 0 else k//2)
        k += 1
    memo_p[n] = s
    return s


def approx_p(n: int) -> int:
    # not using this, just thought i'd preserve it
    # (i was going to use it to estimate ranges)
    c0 = -0.230420145062453320665537
    c1 = -0.0178416569128570889793
    c2 = 0.0051329911273
    c3 = -0.0011129404
    c4 = 0.0009573
    return int(1/(4*n*math.sqrt(3)) * math.exp(math.pi * math.sqrt(2*n/3 + c0 + c1/math.pow(n, 1/2) + c2/n + c3/math.pow(n, 3/2) + c4/math.pow(n, 2))))


class Problem78(object):
    @staticmethod
    def solve():
        for n in range(50, 100000):
            if calc_p(n) % 1000000 == 0:
                return n
        return None

    @staticmethod
    def get_tests():
        return [(None, 55374)]


if __name__ == '__main__':
    print("The answer is", Problem78.solve())
