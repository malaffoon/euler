"""Problem 684 - Project Euler

Inverse Digit Sum

Define s(n) to be the smallest number that has the digit sum of n.
For example s(10) = 19.

Let S(k) = ∑(s(n)) for n=1-k. You are given S(20) = 1074.

Fibonacci sequence is defined as f0=0, f1=1, f2=f1+f0, ...

Find ∑(S(f(i))) for i=2-90.

---------------------------------------------------------------------------------------------------
Sequence of smallest number whose sum of digits is n: https://oeis.org/A051885

s(n) seems straightforward: string of 9's with the appropriate leading digit. But there is a
better way to think about it (refer to OEIS page above). The values in the sequence, s, can be
represented by i * 10^j - 1 (i=1..9, j >= 0). Think of each value as j as a sub-sequence, i.e.
j = 0 -> 0, 1, 2, 3, 4, 5, 6, 7, 8
j = 1 -> 9, 19, 29, 39, 49, 59, 69, 79, 89
j = 2 -> 99, 199, 299, 399, ...
For example, for n=20 (20th term of sequence), j=2,i=3, so s(n) = 3 * 10^2 - 1 = 299.
Note that j = n // 9 and i = n % 9 + 1.

S(k) = SUM{n=1..k} (s(n))
For this sum, we want all the s(n)'s up to k. So we need all the complete sub-sequences below k,
and part of the last sub-sequence. Let q,r=divmod(k,9)
     = SUM{j=0..q-1} SUM{i=1..9} (i * 10^j - 1) + SUM{i=1..r+1} (i * 10^q - 1)

For example, what is S(k) for k = 20?
q, r = 2, 2  (ugh, maybe a bad example)
S(k) = SUM{j=0..1} SUM{i=1..9} (i * 10^j - 1) + SUM{i=1..3} (i * 10^2 - 1)
     = 0+1+2+3+4+5+6+7+8+9+19+29+39+49+59+69+79+89 + 99+199+299
     = 1074

Great, but counting all these terms will be too slow, can we do algebra? Reverse the summations
and we get something like SUM{i=1..9} SUM{j=0..n} (i * 10^j - 1). The inside summation can be
replaced with the singular equation (i * 10^(n+1) - i)/9 - (n+1). So
S(k) = SUM{i=1..9} ((i * 10^q - i)/9 - q) + SUM{i=1..r+1} (i * 10^q - 1)

I've skipped over a messy page of maths and ended up expanding and reducing this to:
S(k) = (5 + (r+1)*(r+2)/2) * 10^q - 9q - r - 6
No, really.

S(20) = 1074
S(49) = 1999945

modulo 1000000007 - do it everywhere to avoid overflow and/or slow maths.
"""
from utils.fibonacci import fibgen
from functools import reduce

mod = 1000000007


def calc_S(k: int) -> int:
    q, r = divmod(k, 9)
    return int(((5 + (r + 1) * (r + 2) / 2) * pow(10, q, mod)) % mod - 9 * q % mod - r - 6) % mod


class Problem684(object):
    @staticmethod
    def solve(limit=90):
        # need to skip the first value in the utils fibonacci (that's just how it is written)
        # probably don't need to worry about doing mod at each step but let's be rigorous
        return reduce(lambda t, fib: (t + calc_S(fib)) % mod, list(fibgen(max_count=limit))[1:])

    @staticmethod
    def get_tests():
        return [(90, 922058210)]


if __name__ == '__main__':
    assert calc_S(20) == 1074
    assert calc_S(49) == 1999945
    print("The answer is", Problem684.solve())
