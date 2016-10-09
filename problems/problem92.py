"""Problem 92 - Project Euler

Square digit chains

A number chain is created by continuously adding the square of the digits in a number
to form a new number until it has been seen before. For example,

  | 44 → 32 → 13 → 10 → 1 → 1
  | 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?

Optimizations
 * after first step, every number will end up at <=567

Approaches:
1. Keep a set of to89's and to1's. Calculate chain for a number until i hit 1, 89, or a known result, then
add to the appropriate set. Return len(to89). Took 45s.

2. For numbers up to 567, do approach 1. Every other number will chain in that range after one chain so
chain once, then lookup answer. Count 'em. Took 13s.

The majority of the execution time is the 10million calls to chain(). We should be able to eliminate calculating
combinations of numbers but that seems more work than the simple chain call.
"""
import itertools as it
import math


class Problem92(object):

    @staticmethod
    def solve(limit=10000000):
        lookup = Problem92.__lookup_table(limit)
        return sum(1 for c in (Problem92.__next_in_chain(i) for i in range(1, limit)) if lookup[c] == 89)

    @staticmethod
    def __next_in_chain(n):
        result = 0
        while n:
            d = n % 10
            result += d*d
            n //= 10
        return result

    @staticmethod
    def __lookup_table(limit):
        # fully calculate lookup table
        lookup_limit = 1 + int(math.log10(limit)) * 9 * 9
        lookup = [0] * lookup_limit
        lookup[1] = 1
        lookup[89] = 89
        for i in range(2, lookup_limit):
            n = i
            while not lookup[n]:
                n = Problem92.__next_in_chain(n)
            lookup[i] = lookup[n]
        return lookup

    # TODO - what about the combinatorial approach?
    # TODO   i'm having trouble counting permutations with leading zeros which have to be discounted
    @staticmethod
    def solve_comb():
        def calc_permutations(s):
            # len(s)! / dup-count1! / dup-count2! - leading-zero-permutations
            return 1

        lookup = Problem92.__lookup_table(10000000)
        total = sum(1 for c in range(1, 100) if lookup[c] == 89)
        for l in range(3, 8):
            for c in (''.join(t) for t in it.combinations_with_replacement('9876543210', l)):
                if lookup[Problem92.__next_in_chain(int(c))] == 89:
                    total += calc_permutations(c)
                    pass
        return total


if __name__ == '__main__':
    print("The answer is", Problem92.solve())
