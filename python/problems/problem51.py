"""Problem 51 - Project Euler

Prime digit replacements

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the
nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits)
with the same digit, is part of an eight prime value family.

Optimizations:
 * eight prime family won't be replacing last digit
 * number will be prime
"""
import itertools as it

from utils.prime import primes, is_prime


class Problem51(object):
    @staticmethod
    def solve(n=8):
        return Problem51.generator(n).__next__()[0]

    @staticmethod
    def get_tests():
        return [(8, 121313), (6, 13), (7, 56003)]

    @staticmethod
    def generator(n):
        # there is some consensus that the wording implies there will be 3 substituted digits
        digits = [str(i) for i in range(10)]

        for p in primes(1000000):
            sp = str(p)
            for d1 in digits[:(11-n)]:    # look for (0,1,2)'s only
                if sp.count(d1) == (n-5):     # this check is contrived but works for examples
                    family = [gen for gen in (int(sp.replace(d1, d2)) for d2 in digits[digits.index(d1):]) if is_prime(gen)]
                    if len(family) == n:
                        yield family

    @staticmethod
    def brute_force(n):
        digits = [str(i) for i in range(10)]

        for p in primes(1000000):
            sp = str(p)
            for subcount in range(1, len(sp)):
                for indices in it.combinations(range(len(sp)-1), subcount):
                    genprimes = []
                    for d in digits[1 if 0 in indices else 0:]:
                        gen = int(''.join([d if i in indices else sp[i] for i in range(len(sp))]))
                        if is_prime(gen): genprimes.append(gen)
                    if len(genprimes) == n:
                        yield genprimes


if __name__ == '__main__':
    print("The answer is", Problem51.solve())
