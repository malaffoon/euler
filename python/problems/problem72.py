"""Problem 72 - Project Euler

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?

Optimizations
 * Clearly, this is the sum of φ(n) for n=[1..d]. Is it fast enough to use that? From problem 69/70, perhaps not.
   Takes about 22s with current implementation of phi().
 * Could probably improve it by caching/recursing for phi's (?)
 * Note, count-by-gcd is two orders of magnitude slower than count-by-phi.

"""
from utils.prime import phi


class Problem72(object):
    @staticmethod
    def solve(maxD=1000000):
        return sum(phi(d) for d in range(maxD, 0, -1))

    @staticmethod
    def get_tests():
        return [(None, 303963552391), (8, 21)]


if __name__ == '__main__':
    print("The answer is", Problem72.solve())
