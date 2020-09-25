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

---------------------------------------------------------------------------------------------------
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
much greater than 1 (number of combinations for 2^84 - 1). Uhmmm, yeah, that's not going
to be correct. The multiplicative nature of this means it'll be a LOT larger than that.

Are there any patterns to this?
f(2^n) = n+1     f(1)=1, f(2)=2, f(4)=3, f(8)=4, ...
f(2^n -1) = 1    f(3)=1, f(7)=1, f(15)=1, ...
"""
from itertools import combinations
from math import ceil, log


powers_of_two = [pow(2, i) for i in range(0, ceil(25 * log(10) / log(2)))]


def minimum_powers(n: int):
    powers = []
    t = len(powers_of_two) - 1
    while n > 0 and t > 0:
        if n >= powers_of_two[t]:
            powers.append(t)
            n -= powers_of_two[t]
        else:
            t -= 1
    return powers


class Problem169(object):
    @staticmethod
    def solve(n=10):
        powers = minimum_powers(n)
        print(f"{n}: {powers} ({len(powers)})")
        # # first solution
        # powers = []
        # for p in range(int(log(n)/log(2)), -1, -1):
        #     t = 2**p
        #     if t > n: continue
        #     powers.append(p)
        #     n -= 2**p
        return 0

    @staticmethod
    def get_tests():
        return [(10, 5), (1e25, None)]


if __name__ == '__main__':
    print("The answer is", Problem169.solve())


"""
532 = 512 + 16 + 4 = 2^9 + 2^4 + 2^2
The first term, 512, has four alternatives that don't "interfere" with the next term:
512
256+256
256+128+128
256+128+64+64
256+128+64+32+32
Likewise, 16 has one alternative:
16
8+8
And 4 has two alternatives:
4
2+2
2+1+1
So, just that gives use 5x2x3 = 30 combinations.
How about interfering alternatives, how can we work those out? 
The next alternative for 512 forces 16 to its alternative:
256+128+64+32+16+16  8+8
Likewise, the next alternative for 16 forces 4 to its alternatives:
8+4+4  2+2
"""