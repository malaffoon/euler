"""Problem 75 - Project Euler

Singular integer right triangles

It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle
in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and
other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly
three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided
right angle triangle be formed?


Optimization
  | L = x + y + z <= 1500000
  | x^2 + y^2 = z^2
  | x < y < z

Now go read about Pythagorean triangles/triples. It is possible to generate primitive pythagorean triples:
  | a = m^2 - n^2
  | b = 2mn
  | c = m^2 + n^2
  | where m, n are coprime and not both odd and m > n > 0
Given any primitive pythagorean triple, multiplying a,b,c by k will give additional pythagorean triples.

So, do a sieve-like approach: generate all triples that meet the conditions and note the resulting L in a list.
When done, the answer is all L's that have a count of 1.
"""
from math import gcd


class Problem75(object):
    @staticmethod
    def solve():
        limit = 1500000
        combos = [0] * limit
        for m in range(2, 1000):
            for n in range(1 if m % 2 == 0 else 2, m, 2):
                if gcd(m,n) != 1: continue
                L = 2*m*(m+n) # a + b + c
                for i in range(L, limit, L):
                    combos[i] += 1

        # print("None", sum(1 for c in combos if c == 0))
        # print("One", sum(1 for c in combos if c == 1))
        # print("Many", sum(1 for c in combos if c >= 1))
        # print("Max", max(combos))
        # None 1144430
        # One 161667
        # Many 355570
        # Max 124

        return sum(1 for c in combos if c == 1)

    @staticmethod
    def get_tests():
        return [(None, 161667)]


if __name__ == '__main__':
    print("The answer is", Problem75.solve())
