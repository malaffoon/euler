import math

import itertools


class ContinuedFraction(object):
    def __init__(self, a0=0, terms=(), infinite=False):
        super().__init__()
        self.a0 = a0
        self.terms = terms
        self.infinite = infinite

    def __repr__(self, *args, **kwargs):
        """Produces a string like [a0;a1,a2,a3] or [a0;(a1,a2,a3)] for infinite"""
        return "[%d;%s%s%s]" % (
        self.a0, "(" if self.infinite else "", ",".join(map(str, self.terms)), ")" if self.infinite else "")

    def convergents(self):
        """Return iterator of convergents

        The convergents are returned as h,k tuples (h=numerator, k=denominator)
        Algorithm from https://en.wikipedia.org/wiki/Continued_fraction#Infinite_continued_fractions
        """
        # pre-convergent and a0 convergent
        convergents = [(1, 0), (self.a0, 1)]
        yield convergents[1]
        # convergents from subsequent terms
        for term in itertools.cycle(self.terms) if self.infinite else self.terms:
            convergents.append(
                (term * convergents[-1][0] + convergents[-2][0], term * convergents[-1][1] + convergents[-2][1]))
            convergents.pop(0)
            yield convergents[1]

    @staticmethod
    def forSqrtOf(n):
        """Calculate the continued fraction for the square root of any natural number.

        Taken from https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion:
          | m(0) = 0, d(0) = 1, a(0) = int(sqrt(n))
          | for x+1:
          | m(x+1) = d(x)a(x) - m(x)
          | d(x+1) = (S - m(x+1)^2) / d(x)
          | a(x+1) = int((a(0) + m(x+1))/d(x+1))

          | stop when a(x+1) = 2 * a(0)
        """

        a0 = int(math.sqrt(n))
        if a0 * a0 == n:
            return ContinuedFraction(a0)
        a, m, d = a0, 0, 1
        terms = []
        while a != (2 * a0):
            m = d * a - m
            d = (n - m * m) / d
            a = int((a0 + m) / d)
            terms.append(a)
        return ContinuedFraction(a0, tuple(terms), True)

    @staticmethod
    def forRational(r):
        """Calculate the continued fraction for a real number

        Example:
          | 3.245 -> 3 49/200  => a0 = 3, f = 49/200
          |   1/f = 200/49  => a = 4, f = 4/49
          |   1/f = 49/4  => a = 12, f = 1/4
          |   1/f = 4/1  => a = 4, f = 0
          |   continued fraction = [3;4,12,4]
        """
        precision_limit = 10 ** 9

        a0 = int(r)
        if a0 == r:
            return ContinuedFraction(a0)
        terms = []
        num, den = float(r - a0).as_integer_ratio()
        while num != 0:
            num, den = den, num
            a, num = divmod(num, den)
            if a > precision_limit: break
            terms.append(a)
        return ContinuedFraction(a0, tuple(terms), False)
