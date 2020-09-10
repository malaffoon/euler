"""Problem 686 - Project Euler

Powers of Two

2^7 = 128 is the first power of two whose leading digits are "12".
The next power of two whose leading digits are "12" is 2^80.

Define p(L,n) to be the nth-smallest value of j such that the base 10 representation of 2^j begins with the digits of L.
So p(12,1)=7 and p(12,2)=80.

You are also given that p(123,45)=12710.

Find p(123,678910).

---------------------------------------------------------------------------------------------------
Brute force seems unlikely for such large powers of 2.
Truncation might work, but the unpredictable error might be an issue.
Going with the mantissa approach combined with expanding the exponentiation. The assertion is that
the first k digits of 2^m are the same as the first k digits of its mantissa.
2^m = 10^(m log(2))
let x = m log(2) and f(x) = x - floor(x)
then mantissa of 2^m = mantissa of 10^f(x)
constrain the mantissa to be within 1.230 and 1.23999999

Numba was a HUGE help here, improved time from 38s to 240ms!
"""
import math
import numba


class Problem686(object):
    @staticmethod
    @numba.jit
    def solve(L: int, n: int) -> int:
        # how much to divide L by to make it look like a mantissa?
        div = pow(10, math.floor(math.log10(L)))
        # what is the range of the mantissa to match L?
        lo = math.log10(L / div)
        hi = math.log10((L + 1) / div)
        log2 = math.log10(2)
        # numba doesn't know about itertools.count() so just use a big range
        for m in range(1, 999999999):
            x = m * log2
            x -= int(x)
            if lo <= x < hi:
                n -= 1
                if n == 0:
                    return m

    @staticmethod
    def get_tests():
        return [((12, 1), 7), ((12, 2), 80), ((123, 45), 12710), ((123, 678910), 193060223)]


if __name__ == '__main__':
    print("The answer is", Problem686.solve(123, 678910))
