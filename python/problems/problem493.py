"""Problem 493 - Project Euler

Under The Rainbow

70 coloured balls are placed in an urn, 10 for each of the seven rainbow colours.
What is the expected number of distinct colours in 20 randomly picked balls?
Give your answer with nine digits after the decimal point (a.bcdefghij).

---------------------------------------------------------------------------------------------------
This is one of those "one minus" probability problems.

First off, there are 70C20 (~161884603662657888) total possible combinations of balls.
For any one color, the combinations where it isn't part of the solution is 60C20, i.e. the 20 balls
are chosen from the 60 other-colored balls. The probability of this happening is 60C20 / 70C20.
So the odds that the color IS in the solution is (1 - 60C20 / 70C20). Adding that up for all 7 colors
gives the final answer.

Because python is nice, we don't need to do anything special for nCr.
"""
import math


class Problem493(object):
    @staticmethod
    def solve():
        def nCr(n,r):
            return int(math.factorial(n) / math.factorial(r) / math.factorial(n-r))

        return 7 * (1 - nCr(60, 20) / nCr(70, 20))

    @staticmethod
    def get_tests():
        return [(None, 6.818741802)]


if __name__ == '__main__':
    print("The answer is", Problem493.solve())