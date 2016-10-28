"""Problem 65 - Project Euler

Convergents of e

(the continued fraction stuff)
"""
from itertools import chain
from math import gcd


class Problem65(object):
    @staticmethod
    def solve(n=100):
        def reduce(cf):
            """reduce a continued fraction to a simple fraction

            cf -> (n, (f1, f2, f3, ...))
            result -> (num, den)

            For example, reduce((2, (1,2,1,1,4,1,1,6,1)) = 1457/536
            """

            def helper(src, f=(0,1)):
                """src is remaining fraction values in a tuple, f is current (n,d) fraction

                Recursively pulls the tail off the tuple, returning 1/(tail + (n,d))
                """
                if src:
                    src, tail = src[0:-1], src[-1]
                    f = f[1], tail * f[1] + f[0]
                    return helper(src, f)
                return f

            # deal with continued fraction part
            f = helper(list(cf[1]))

            # now combine with whole number into a reduced fraction
            result = cf[0] * f[1] + f[0], f[1]
            g = gcd(result[0], result[1])
            return result[0] // g, result[1] // g

        # calculate the continued fraction up to the requested number of terms (-1 for whole number)
        c = reduce((2, chain.from_iterable((1, 2*(k+1), 1) for k in range((n-1)//3))))

        # all that is desired is the sum of the digits of the numerator of the convergent
        return sum(int(d) for d in str(c[0]))

    @staticmethod
    def get_tests():
        return [(100, 272), (10, 17)]


if __name__ == '__main__':
    print("The answer is", Problem65.solve())
