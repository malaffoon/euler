"""Problem 33 - Project Euler

Digit cancelling fractions

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing
two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

from functools import reduce
from math import gcd


class Problem33(object):
    @staticmethod
    def solve():
        fractions = []
        for d in range(11, 100):
            for n in range(10, d):
                if float(n) / float(d) == Problem33.digit_cancelled(n, d):
                    fractions.append((n, d))
        product = reduce(lambda f1, f2: (f1[0] * f2[0], f1[1] * f2[1]), fractions, (1, 1))
        return product[1] // gcd(product[0], product[1])

    @staticmethod
    def digit_cancelled(n, d):
        """Returns the value of the fraction n/d if it can be digit cancelled

        For example, 49/98 -> 4/8 so this will return 0.5.
        Returns None if there are no common digits, the common digit is 0, both digits are common, or
        resulting faction is invalid, e.g 30/50, 37/85, 45/54, 15/50
        """
        if n < 10 or n > 99 or d < 10 or d > 99: raise ValueError
        nstr, dstr = str(n), str(d)
        if nstr[0] in dstr and nstr[1] in dstr: return None
        for i in (i for i in [0, 1] if nstr[i] != '0' and nstr[i] in dstr):
            num = nstr[1 - i]
            den = dstr[1 - i if nstr[i] == dstr[i] else i]
            if num != '0' and den != '0': return float(num) / float(den)
        return None


if __name__ == '__main__':
    print("The answer is", Problem33.solve())
