"""Problem 58 - Project Euler

Spiral primes

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

  | 37 36 35 34 33 32 31
  | 38 17 16 15 14 13 30
  | 39 18  5  4  3 12 29
  | 40 19  6  1  2 11 28
  | 41 20  7  8  9 10 27
  | 42 21 22 23 24 25 26
  | 43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more
interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed.
If this process is continued, what is the side length of the square spiral for which the ratio of primes along
both diagonals first falls below 10%?

Algorithm:
 * r = ring, 0=degenerate
 * n = side length = 2r+1
 * corners = n*n, n*n-2r, n*n-4r, n*n-6r
So, just keep track of total corners and how many are prime
"""
import itertools as it

from utils.prime import is_prime


class Problem58(object):
    @staticmethod
    def solve():
        # start with degenerate case
        count, prime = 1, 0
        for r in it.count(1):
            n = 2 * r + 1
            count += 4
            prime += sum(1 for c in (n * n - k * r for k in [0, 2, 4, 6]) if is_prime(c))
            if prime / count < 0.10:
                return n

    @staticmethod
    def get_tests():
        return [(None, 26241)]


if __name__ == '__main__':
    print("The answer is", Problem58.solve())
