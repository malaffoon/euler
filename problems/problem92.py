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

class Problem92(object):
    @staticmethod
    def solve():
        def chain(n):
            result = 0
            while n:
                d = n % 10
                result += d*d
                n //= 10
            return result

        # fully calculate lookup table
        lookup = [0] * 568
        lookup[1] = 1
        lookup[89] = 89
        for i in range(2, 568):
            n = i
            while True:
                if n == 1 or lookup[n] == 1:
                    lookup[i] = 1
                    break
                if n == 89 or lookup[n] == 89:
                    lookup[i] = 89
                    break
                n = chain(n)

        # now, count the ones that hit 89
        return sum(1 for c in (chain(i) for i in range(1, 10000000)) if lookup[c] == 89)


if __name__ == '__main__':
    print("The answer is", Problem92.solve())
