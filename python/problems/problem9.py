"""Problem 9 - Project Euler

Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
   a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Algebra can be used to calculate values.
Given n (1000)
For any a: b = (n**2 - 2*a*n) / (2*n - 2*a)
"""

import math


class Problem9(object):
    @staticmethod
    def solve(n=1000):
        # takes about 0.12ms for n=1000
        for a in range(1, n // 3):
            b = (n**2 - 2 * a * n) / (n - a) / 2
            if b.is_integer():
                b = int(b)
                return a * b * (n-a-b)

    @staticmethod
    def solve_loop(n=1000):
        # takes about 60ms for n=1000
        for a in range(1, n // 3):
            for b in range(a + 1, (n - a) // 2 + 1):
                c = math.sqrt(a ** 2 + b ** 2)
                if c.is_integer() and (a + b + c) == n:
                    return int(a * b * c)

    @staticmethod
    def solve_literal(n=1000):
        # takes about 2.5s for n=1000
        for a in range(1, n // 3):
            for b in range(a + 1, (n - a) // 2 + 1):
                for c in range(b + 1, n):
                    if a + b + c < n: continue
                    if a + b + c > n: break
                    if (a * a + b * b) == c * c:
                        return a * b * c

    @staticmethod
    def get_tests():
        return [(1000, 31875000), (12, 60)]


if __name__ == '__main__':
    print("The product abc for the triplet is", Problem9.solve())
