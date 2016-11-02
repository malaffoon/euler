"""Problem 243 - Project Euler

Resilience

A positive fraction whose numerator is less than its denominator is called a proper fraction.
For any denominator, d, there will be d−1 proper fractions; for example, with d = 12:
1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12 .

We shall call a fraction that cannot be cancelled down a resilient fraction.
Furthermore we shall define the resilience of a denominator, R(d), to be the ratio of its proper
fractions that are resilient; for example, R(12) = 4/11 .
In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10 .

Find the smallest denominator d, having a resilience R(d) < 15499/94744 .

Algorithm
 - 15499/94744 = 0.1635881955585578

Recall that phi(d) is the number of numbers less than d that are relatively prime
to d. So R(d) can be seen to be phi(d)/(d-1). And the interwebs tell us that phi(d)
is d * PROD{p|d}(1 - 1/p) where p is from the set of prime factors of d. We are trying
to find a minimal value of resilience so, moving things around, we are trying to limit:
  | d/(d-1) * PROD{p|d}((p-1)/p)
This isn't particularly fast to calculate because we have to find the factors of d.
But what if we set d to be the product of sequential primes? Then calculating R(d)
is fast and easy. We can quickly find the sequence of primes where R(d) is less than
the target minimum, then back off one:
  | for primes 2..29 -> d = 6469693230, and R(d) = 0.1579472231263656
  | for primes 2..23 -> d = 223092870, and R(d) = 0.16358819608886738
Now we have a good starting point for d, it won't be smaller than 223092870. And
since it is so dang close to the limit, it probably won't be much bigger than that.
So multiply it by small factors (primes or prime multiples) until we hit the limit.

"""
from functools import reduce
from operator import mul

from utils.prime import factors, primes


class Problem243(object):
    @staticmethod
    def solve(rlimit=15499 / 94744):
        def find_start(rlimit):
            ps = list(primes(50))
            for limit in range(1, len(ps)):
                d = reduce(mul, ps[:limit], 1)
                if reduce(mul, map(lambda p: (p-1)/p, ps[:limit]), 1) * d / (d-1) < rlimit:
                    return reduce(mul, ps[:limit-1], 1)

        def resilience(d):
            return reduce(mul, map(lambda p: (p - 1) / p, set(factors(d))), 1) * d / (d - 1)

        start = find_start(rlimit)
        for m in range(2, 20):
            d = m * start
            if resilience(d) < rlimit:
                return d

    @staticmethod
    def get_tests():
        return [(None, 892371480), (4/10, 12)]


if __name__ == '__main__':
    print("The answer is", Problem243.solve())
