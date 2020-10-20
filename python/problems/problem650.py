"""Problem 650 - Project Euler

Divisors of Binomial Product

Let B(n) = PROD{k=0..n) (nCk), a product of binomial coefficients.
For example, B(5) = 5C0 x 5C1 x 5C2 x 5C3 x 5C4 x 5C5 = 1 x 5 x 10 x 10 x 5 x 1 = 2500.

Let D(n) = SUM{d|B(n)} (d), the sum of the divisors of B(n).
For example, the divisors of B(5) are 1, 2, 4, 5, 10, 20, 25, 50, 100, 125, 250, 500, 625, 1250, 2500.
So D(5) = 5467.

Let S(n) = SUM(k=1..n) (D(k)).

You are given S(5) = 5736, S(10) = 141740594713218418, S(100) mod 1000000007 = 332792866.

Find S(20000) mod 1000000007.

---------------------------------------------------------------------------------------------------
Sequence of product of Pascal's triangle rows: https://oeis.org/A001142
There are a few formulae for it, not sure if any are useful.

Even if they are, finding the sum of the divisors seems to be the sticking point of this problem.



modulo 1000000007 - do it everywhere to avoid overflow and/or slow maths.
"""
from utils.fibonacci import fibgen
from functools import reduce

mod = 1000000007


class Problem650(object):
    @staticmethod
    def solve(n):
        return None

    @staticmethod
    def get_tests():
        return [(None, None)]
        # return [(5, 5736), (10, 721034267), (100, 332792866), (20000, None)]


if __name__ == '__main__':
    print("The answer is", Problem650.solve(20000))
