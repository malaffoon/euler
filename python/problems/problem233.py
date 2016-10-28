"""Problem 233 - Project Euler

Lattice points on a circle

Let f(N) be the number of points with integer coordinates that are on a circle
passing through (0,0), (N,0), (0,N), and (N,N).

It can be shown that f(10000) = 36.

What is the sum of all positive integers N ≤ 10^11 such that f(N) = 420 ?


Equation of circle is:
  | (x - N/2) + (y - N/2) = N^2 / 2
x,y will be in range:
  | N(1/2 +- 1/sqrt(2)) = (-0.20710678118655 -> 1.20710678118655) * N

Optimizations:
Clearly brute-force isn't going to cut it
"""
import math

D = 1 / math.sqrt(2) - 1 / 2  # 0.20710678118655


class Problem233(object):
    @staticmethod
    def f(n):
        def possible_range(n):
            return range(math.ceil(-D * n), math.ceil((1 + D) * n))

        def solve_for_y(n, x):
            m = math.sqrt((n*n/2) - (x - n/2)*(x - n/2))
            return n/2-m, n/2+m

        count = 0
        for x in possible_range(n):
            y1, y2 = solve_for_y(n, x)
            if y1.is_integer(): count += 1
            if y2.is_integer(): count += 1
        return count

    @staticmethod
    def solve():
        for n in range(1, 10000):
            f = Problem233.f(n)
            if f > 35: print(n, f)
        return 0

    @staticmethod
    def get_tests():
        return []


if __name__ == '__main__':
    print(Problem233.f(10000))
    print("The answer is", Problem233.solve())
