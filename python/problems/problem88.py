"""Problem 88 - Project Euler

Product-sum numbers

A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers,
{a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number.
The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 × 2 = 2 + 2
k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30;
note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2≤k≤12000?

---------------------------------------------------------------------------------------------------
As k increases, the numbers are going to be a bunch of 1's and a couple factors.

What are the limits of mps for a given k?
k is the min limit, i think. You just can't have less than the sum of k 1's.
2k is the max, i think. I have trouble thinking about the maximum minimum value but:
mps = 2k => 1x1x1...x2xk = 2 + k + (k-2)1's

I suspect that generating the numbers from factors will be more efficient than factoring and partitioning.

2x2=4 <= 2+2 so can't extend by adding 1's
2x3=6  > 2+3 so can extend by adding a 1, 1x2x3=1+2+3, so 6 is a product-sum for k=3
2x4=8  > 2+4 so can extend by adding 1's, 1x1x2x4=1+1+2+4, so 8 is a product-sum for k=4
- do we factor each value here? or let a later generator find 2x2x2?
2x5=10 > 2+5 so can extend by adding 1's, 1x1x1x2x5=1+1+1+2+5, so 10 is a product-sum, but not the smallest for k=5
3x3=9  > 3+3 => 1x1x1x3x3=1+1+1+3+3=9, k=5
3x4=12 => 1x1x1x1x1x3x4=1+1+1+1+1+3+4=12, k=7
3x2x2 => 1x1x1x1x1x2x2x3=1+1+1+1+1+2+2+3=12, k=8

How far do we have to go to get to k=12000?
How large should the integers get? vs using more integers?

Using hard-coded limits is working but taking quite a while, is there a better approach? Improvements?
If we generate the factors directly, it will work better. For example, for two factors we want:
(2,2),(2,3),...,(2,12000),(3,3),(3,4),...,(3,8000),(4,4),...,(4,6000),...,(109,109),...,(109,220)
Then for three factors we want:
(2,2,2),(2,2,3),...,(2,2,6000),(2,3,3),(2,3,4),...,(2,3,4000),...
And we go up to log2(24000) factors, i.e. (2,2,2,2,2,2,2,2,2,2,2,2,2,2)

Tricky bit is coding the "increment" of the factors ...
"""
from functools import reduce
from operator import mul
import math


class Problem88(object):
    @staticmethod
    def solve(limit=12000):
        mps = [0, 0] + [2*k for k in range(2, limit+1)]  # list of smallest N (minimal product sum), indexed by k
        prod_max = 2 * limit    # this can probably be lower, not sure how to calculate optimum
        # manually generate combinations from 2 factors up to log2 of the limit
        for num_factors in range(2, 1 + math.ceil(math.log2(limit))):
            factors = [2] * num_factors
            shift_f = num_factors - 1  # current "register" for shifting
            while True:
                prod = reduce(mul, factors, 1)
                if prod <= prod_max:
                    k = prod - sum(factors) + num_factors
                    if k <= limit and prod < mps[k]:
                        mps[k] = prod
                    shift_f = num_factors - 1  # reset shift register
                    factors[shift_f] += 1      # and increment factors
                elif shift_f == 0:
                    break   # can't shift, we're done with these factors
                else:
                    shift_f -= 1
                    factors[shift_f] += 1
                    for f in range(shift_f + 1, num_factors):
                        factors[f] = factors[shift_f]
        # extract goofy sum needed for answer
        return sum(set(mps))

    @staticmethod
    def get_tests():
        return [(6, 30), (12, 61), (12000, 7587457)]


if __name__ == '__main__':
    print("The answer is", Problem88.solve())
