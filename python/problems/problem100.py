"""Problem 100 - Project Euler

Arranged probability

If a box contains twenty-one coloured discs, composed of fifteen blue discs and
six red discs, and two discs were taken at random, it can be seen that the
probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue
discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total,
determine the number of blue discs that the box would contain.


B/N x (B-1)/(N-1) = 1/2

Solve that for B and you get the binomial: B^2 - B - N(N-1)/2 = 0 which has
solutions B = (1 +- sqrt(1 + 2N(N-1))) / 2. For that to be an integer then
the sqrt part, 1 + 2N(N-1), must be a perfect square.

For convenience, let y^2 = 1 + 2N(N-1), so b = (1+y)/2

Also, because the numbers are large, we can say that B ~ N / srqt(2).

There will probably be an issue with precision, try to stick to integers.

Tried the obvious: n=1e12,... calculate y, check that it is integer.
I had the calculation wrong but it still seems slow-ish.

How about loop over b instead? Solve the equations the other way and
n = (1 +- sqrt(1 + 8b(b-1)))/2
Let y^2 = 1 + 8b(b-1) which must be a perfect square
n = (1+y)/2
oh, and b must be odd

First few generate quickly: n,b =
4 3
21 15
120 85
697 493
4060 2871
23661 16731
137904 97513
803761 568345
4684660 3312555
27304197 19306983
159140520 112529341
927538921 655869061
"""
import itertools

from utils import mathex


class Problem100(object):
    @staticmethod
    def solve():
        # start with first odd number above 1e12/sqrt(2)
        b0 = int(1e12 / 1.414)
        if b0 % 2 == 0: b0 += 1
        print(b0)
        for b in itertools.count(start=b0, step=2):
            if (b-1) % 10000000 == 0: print(b)
            y2 = 1 + 8 * b * (b-1)
            y = mathex.isqrt(y2)
            if y*y == y2:
                n = int((1+y)/2)
                print(n, b)
                return b
        return None

    @staticmethod
    def get_tests():
        return [(None, None)]
    

if __name__ == '__main__':
    # Problem100.samples()
    print("The answer is", Problem100.solve())
