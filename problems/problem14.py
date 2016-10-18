"""Problem 14 - Project Euler

   Longest Collatz sequence

   The following iterative sequence is defined for the set of positive integers:
     n → n/2 (n is even), n → 3n + 1 (n is odd)

   Using the rule above and starting with 13, we generate the following sequence:
     13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
   It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
   Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

   Which starting number, under one million, produces the longest chain?
"""

from utils import collatz


class Problem14(object):
    @staticmethod
    def solve():
        # this solution caches lengths to short-circuit calculations
        # it gets the answer in 3-4 seconds on my laptop
        # however, it has to in-line the collatz sequencing
        lengths = {1: 1, 2: 2, 4: 3, 8: 4, 16: 5}  # value -> collatz sequence length
        longest = 5
        max_value = 16
        for v in range(1000000):
            l = 0
            c = v
            while c:
                if c in lengths:
                    l += lengths[c]
                    lengths[v] = l
                    if l > longest:
                        longest = l
                        max_value = v
                    break
                l += 1
                c = collatz.next_collatz(c)
        return max_value

    @staticmethod
    def solve2():
        # brute force it, takes about 30 seconds to run on my laptop
        longest = 0
        max_value = 0
        for v in range(1000000):
            l = sum(1 for _ in collatz.generator(v))
            if l > longest:
                print("new longest value", v, l)
                longest = l
                max_value = v
        return max_value

    @staticmethod
    def get_tests():
        return [(None, 837799)]


if __name__ == '__main__':
    print("The starting number, under one million, that produces the longest Collatz sequence is", Problem14().solve())
