"""Problem 233 - Project Euler

Lattice points on a circle

Let f(N) be the number of points with integer coordinates that are on a circle
passing through (0,0), (N,0), (0,N), and (N,N).

It can be shown that f(10000) = 36.

What is the sum of all positive integers N ≤ 10^11 such that f(N) = 420 ?


Equation of circle is:
  | (x - N/2)^2 + (y - N/2)^2 = N^2 / 2
x,y will be in range:
  | N(1/2 +- 1/sqrt(2)) = (-0.20710678118655 -> 1.20710678118655) * N

There is a theory in number theory that might help here.
see http://math.stackexchange.com/questions/17496/number-of-integer-solutions-of-x2-y2-k
For a number, n, that can be represented as a product of its prime factors:
  | n = 2^α ∏p^β ∏q^γ
  |    p is set of prime factors with mod4 == 1
  |    q is set of prime factors with mod4 == 3
This number can be represented as the sum of two squares iff all exponents γ are even.
Further, the number of ordered pairs (x,y) of integers such that x^2 + y^2 = n, R(n), is:
  | R(n) = 4 ∏(β+1)

How does this help us? Well, the circle equation can be simplified. For these purposes
translation of the origin won't affect the result:
  | x^2 + y^2 = N^2 / 2 = T
Applying the theory to T and the requirement that f(T) = 420:
  | R(T) = 4 ∏(β+1) = 420  =>  ∏(β+1) = 105
The only ways to factor 105 are {(3,5,7),(3,35),(5,21),(7,15),(105)}. That implies that
the βs must be {(2,4,6),(2,34),(4,20),(6,14),(104)}. Since T < 10^22, and the first
three p primes are 5,13,17, we can discard some of those leaving {(2,4,6),(4,20),(6,14)}
as possible sets of βs. At the same time, we want sqrt(2T) to be an integer < 10^11.
For that to be true, β and γ must be even and α must be odd. So we are looking for
numbers that have either two or three p-prime factors with exponents from the set of
{(2,4,6),(4,20),(6,14)}, and we can multiply by q-prime factors with even exponents
and/or 2 with odd exponents.

Hint from interwebs, there are 5422629 solutions
"""
import math

from functools import reduce

from operator import mul

from utils.prime import primes

D = 1 / math.sqrt(2) - 1 / 2  # 0.20710678118655


class Problem233(object):
    @staticmethod
    def f(n):
        def possible_range(n):
            return range(math.ceil(-D * n), math.ceil((1 + D) * n))

        def solve_for_y(n, x):
            m = math.sqrt((n * n / 2) - (x - n / 2) * (x - n / 2))
            return n / 2 - m, n / 2 + m

        points = []
        for x in possible_range(n):
            y1, y2 = solve_for_y(n, x)
            if y1.is_integer(): points.append((x, y1))
            if y2.is_integer(): points.append((x, y2))
        # for point in points: print(point)
        return len(points)

    @staticmethod
    def helper(maxT=pow(10, 22) / 2, betas=(6, 4, 2)):
        # we know the first three p_primes are 5, 13, 17 so smallest candidate can be calculated:
        smallest_candidate = reduce(mul, map(lambda t: pow(t[0], t[1]), zip((5, 13, 17), betas)))
        print(smallest_candidate)

        # create list of allowed multipliers (2 to odd exponents, 'q' primes to exponent 2,4,6...)
        # the most we can multiple the smallest by and stay under the problem limit
        multiplier_limit = maxT / smallest_candidate
        log_limit = math.log(multiplier_limit)
        # bit convoluted: trying to find all combinations of 2^α ∏q^γ for odd α and even γ below multiplier limit
        q_multipliers = []
        for q in (q for q in primes(int(math.sqrt(multiplier_limit))) if q % 4 == 3):
            allowed = [q ** i for i in range(int(log_limit / math.log(q) / 2) * 2, 0, -2)]
            if not allowed: break
            q_multipliers.extend(p for p in (a*m for a in allowed for m in q_multipliers) if p <= multiplier_limit)
            q_multipliers.extend(allowed)
        multipliers = []
        for t in (2 ** i for i in range(int(log_limit / math.log(2) / 2) * 2 + 1, 0, -2)):
            multipliers.append(t)
            multipliers.extend(p for p in (t*m for m in q_multipliers) if p <= multiplier_limit)
        multipliers.sort()
        print(len(multipliers), multipliers)

        def count_em(base):
            c = 0
            s = 0
            m_limit = maxT / base
            for m in multipliers:
                if m > m_limit: break
                T = m * base
                c += 1
                s += int(math.sqrt(2*T))
            return c, s

        # permute them in groups of 3
        countN = 0
        sumN = 0
        p0_limit = int(0.5 + math.pow(maxT, 1 / betas[0]))
        for p0 in (p for p in primes(p0_limit) if p % 4 == 1):
            p0f = pow(p0, betas[0])
            p1_limit = int(0.5 + math.pow(maxT / p0f, 1 / betas[1]))
            for p1 in (p for p in primes(p1_limit) if p % 4 == 1 and p != p0):
                p1f = p0f * pow(p1, betas[1])
                if len(betas) == 2:
                    result = count_em(p1f)
                    countN, sumN = countN + result[0], sumN + result[1]
                else:
                    p2_limit = int(0.5 + math.pow(maxT / p1f, 1 / betas[2]))
                    for p2 in (p for p in primes(p2_limit) if p % 4 == 1 and p != p0 and p != p1):
                        p2f = p1f * pow(p2, betas[2])
                        result = count_em(p2f)
                        countN, sumN = countN + result[0], sumN + result[1]
        print("count =", countN, ", sum = ", sumN)
        return countN, sumN

    @staticmethod
    def solve():
        return Problem233.helper(pow(10, 22) / 2, [6, 4, 2])[1] + \
               Problem233.helper(pow(10, 22) / 2, [14, 6])[1] + \
               Problem233.helper(pow(10, 22) / 2, [20, 4])[1]

    @staticmethod
    def get_tests():
        return [(None, 137632180640734102)]


if __name__ == '__main__':
    print(Problem233.solve())
    # print("The answer is", Problem233.solve())
