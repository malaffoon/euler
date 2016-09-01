"""Problem 5 - Project Euler

   Smallest multiple

   2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

   What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from utils.mathex import lcm


class Problem5(object):
    @staticmethod
    def solve():
        return lcm(range(1,20))


if __name__ == '__main__':
    print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is", Problem5.solve())
