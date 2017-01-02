"""Problem 74 - Project Euler

Digit factorial chains

The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169;
it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

Optimization
 * brute force did find the answer in less than a minute but it was slow
   * could memoize based on unique digits in number (so, map of order-independent hash of digits -> chain length)
 * may not be safe but it appears the longest sequence is the same for all of them, hitting 367945/54 - 368790
   so it can be made a lot faster by just looking for 368790 as the third term; takes about 5s
"""
import math
from utils.mathex import digits


class Problem74(object):
    @staticmethod
    def solve():
        # cache digit factorials
        factorials = list(map(math.factorial, range(0, 10)))

        def next(n):
            return sum(factorials[d] for d in digits(n))

        return sum(1 for d in range(1, 1000000) if next(next(d)) == 368790)

    @staticmethod
    def get_tests():
        return [(None, 402)]


if __name__ == '__main__':
    print("The answer is", Problem74.solve())
