"""Problem 684 - Project Euler

Inverse Digit Sum

Define s(n) to be the smallest number that has the digit sum of n.
For example s(10) = 19.

Let S(k) = ∑(s(n)) for n=1-k. You are given S(20) = 1074.

Fibonacci sequence is defined as f0=0, f1=1, f2=f1+f0, ...

Find ∑(S(f(i))) for i=2-90.
"""

from utils.fibonacci import fibgen, Fibonacci


class Problem684(object):
    @staticmethod
    def solve(limit=90):
        # need to skip the first value in the utils fibonacci (that's just how it is written)
        fibs = list(fibgen(max_count=limit))[1:]
        # hardcode the results from the first fibonacci to make loop/indexing easier
        # result = 1
        # prevS = 1
        # for i, fib in enumerate(fibs[1:], start=1):
        #     S = prevS + sum(Problem684.s(n+1) for n in range(fibs[i-1], fib))
        #     result += S
        #     prevS = S
        #     print(f"{i},{fib}: S={S}, result={result}, check={result % 1000000007}")
        #
        # return result % 1000000007
        return None

    @staticmethod
    def s(n: int) -> int:
        # what is the fastest way to do this?
        quotient, remainder = divmod(n, 9)
        return remainder * pow(10, quotient) + sum(9 * pow(10, q) for q in range(0, quotient))

    @staticmethod
    def get_tests():
        return [(None, None)]


if __name__ == '__main__':
    print("The answer is", Problem684.solve())



"""
f(i) for i=2-90  is 1,2,3,5,8,13,...; fibgen() starts with one value before this sequence
  f(2) = 1, f(90) = 2880067194370816120
S(f) is ∑(s(n)), e.g. S(13) = ∑s(n) for n=1-13
"""

