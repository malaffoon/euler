"""Problem 87 - Project Euler

Prime power triples

The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28.
In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?

Algorithm:
 * combinatorial problem with inputs as the prime square, prime cube, and prime fourth powers?
   * need all primes that are less than ceil(sqrt(limit - 2^3 - 2^4))
   * all prime squares that are less than (limit - 2^3 - 2^4)  (908)
   * all prime cubes that are less than (limit - 2^2 - 2^4)  (73)
   * all prime fourths that are less than (limit - 2^2 - 2^3)  (23)
 * brute force takes about 450ms to dedup and count
"""
from itertools import takewhile
from math import sqrt, ceil

from utils.prime import primes


class Problem87(object):
    @staticmethod
    def solve(limit=50000000):
        ps = tuple(primes(ceil(sqrt(limit - 24))))
        # cache squares (908) and cubes (73); don't bother with fourths (23) since a single iteration
        squares = tuple(takewhile(lambda s: s < (limit-24), (p*p for p in ps)))
        cubes = tuple(takewhile(lambda c: c < (limit-20), (p*p*p for p in ps)))
        values = set()  # need to dedup the answers
        for fourth in takewhile(lambda f: f < (limit-12), (p*p*p*p for p in ps)):
            for cube in cubes:
                if cube + fourth >= limit: break
                for square in squares:
                    if square + cube + fourth >= limit: break
                    values.add(square+cube+fourth)
        return len(values)

    @staticmethod
    def get_tests():
        return [(None, 1097343), (50, 4)]


if __name__ == '__main__':
    print("The answer is", Problem87.solve())
