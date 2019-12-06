"""Problem 493 - Project Euler

Under The Rainbow

70 coloured balls are placed in an urn, 10 for each of the seven rainbow colours.
What is the expected number of distinct colours in 20 randomly picked balls?
Give your answer with nine digits after the decimal point (a.bcdefghij).

Total number of combinations is 70C20 ~ 161884603662657888  (10e17)
The number of ways to get:
1 color = 0
2 colors = 20C20 x 7C2 = 1 x 21
3 colors = 30C20 x 7C3 - (# for 2 colors)
4 colors = 40C20 x 7C4 - (# for 2-3 colors)
5 colors = ...
6 colors = ...
7 colors = 70C20 x 7C7 - (# for 2-6 colors)
"""
import math
import random

import cProfile
import timeit


class Problem493(object):
    @staticmethod
    def solve():
        guesses = [0, 0, 1, 30045014, 137816483805, 46991365715140, 4144715293561535, 157692759156852393]
        answer = 0
        for c in range(1, len(guesses)):
            answer += c * guesses[c]
        return answer / 161884603662657888

    @staticmethod
    def solve2():
        """Can we just solve this with statistics and expected value?

        6.8125982953816635    6.812598295 is not correct  <-- subtracting previous

        Running a random simulator converges on 6.818735...
        So clearly there is something wrong with my math but i can't figure it ... sigh
        """
        def nCr(n,r):
            return math.factorial(n) / math.factorial(r) / math.factorial(n-r)

        # generate total count for each number of colors
        combos = [0]*8
        for c in range(2, 8):
            combos[c] = nCr(c*10, 20) * nCr(7, c)
        # now correct each count by subtracting count of previous number of colors
        for c in range(7, 1, -1):
            combos[c] -= combos[c-1]
        print(combos, sum(combos))
        print(sum(c*cnt for c,cnt in enumerate(combos)) / sum(combos))


    @staticmethod
    def solve1():
        """Sampling approach, but to get the required precision will take a while.
        The performance bottleneck is random.sample.

        10e6 gives ~6.818835: [0, 0, 0, 0, 31, 5975, 169122, 824872] 1000000
        10e7 gives ~6.8185894: [0, 0, 0, 0, 276, 60402, 1692474, 8246848] 10000000
        10e8 gives ~6.81879812: [0, 0, 0, 0, 2984, 602404, 16906428, 82488184] 100000000 (2100s)
        seems to be converging on 6.818735/6...
        6.8187357074375 [0, 0, 0, 218, 952687, 192798342, 5412001745, 26394247008] 32000000000
        6.818736432456648 [0, 0, 0, 234, 1030476, 208455415, 5851716243, 28538797632] 34600000000
        :return:
        """
        balls = ('r', 'o', 'y', 'g', 'b', 'i', 'v') * 10
        counts = [0]*8
        for _ in range(10):
            for _ in range(10**5):
                counts[len(set(random.sample(balls, 20)))] += 1
            print(sum(c*cnt for c,cnt in enumerate(counts)) / sum(counts), counts, sum(counts))

        return None

    @staticmethod
    def get_tests():
        return [(None, None)]


if __name__ == '__main__':
    # Problem493.solve2()
    # cProfile.run('Problem493.solve1()')
    print(timeit.timeit('Problem493().solve1()', setup='from problems.problem493 import Problem493', number=1))
    # Problem493.solve1()
    # print("The answer is", Problem493.solve())
