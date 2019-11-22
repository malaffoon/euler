"""Problem 169 - Project Euler

Exploring the number of different ways a number can be expressed as a sum of powers of 2

Define f(0)=1 and f(n) to be the number of different ways n can be expressed as a sum of integer powers
of 2 using each power no more than twice.

For example, f(10)=5 since there are five different ways to express 10:

  | 1 + 1 + 8
  | 1 + 1 + 4 + 4
  | 1 + 1 + 2 + 2 + 4
  | 2 + 4 + 4
  | 2 + 8

What is f(10^25)?

Optimizations
 * 2^x < 10^25  => x = 83

find the solution with fewest values then use math to decompose those arguments
 | 10: [3,1]
 | 10^25 : [83, 78, 74, 72, 71, 68, 66, 64, 60, 58, 57, 52, 50, 40, 38, 35, 30, 27, 25]

there are n+1 ways to reduce 2^n:
  | 2^0: 1
  | 2^1: 2, 1+1
  | 2^2: 4, 2+2, 2+1+1
  | 2^3: 8, 4+4, 4+2+2, 4+2+1+1
  | ...

when combining two arguments, e.g. 16+4, combinations are eliminated based on smaller arg
due to rule (no more than twice) and duplication to the tune of 1 + n(n + 1)
  | 2^0: 1 + 0 = 1
  | 2^1: 2 + 1 = 3
  | 2^2: 5 + 2 = 7
  | 2^3: 10 + 3 = 13
  | ...

so, how do combinations across many arguments get eliminated?

Pretty sure the answer will be <= 85 (number of combinations for 2^84) and it will be
much greater than 1 (number of combinations for 2^84 - 1).
"""
from math import log


class Problem169(object):
    @staticmethod
    def solve(n=10):
        # first solution
        powers = []
        for p in range(int(log(n)/log(2)), -1, -1):
            t = 2**p
            if t > n: continue
            powers.append(p)
            n -= 2**p
        return 0

    @staticmethod
    def get_tests():
        return [(None, 0)]


if __name__ == '__main__':
    print("The answer is", Problem169.solve())
