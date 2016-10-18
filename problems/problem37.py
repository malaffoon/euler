"""Problem 37 - Project Euler

Truncatable primes

The number 3797 has an interesting property. Being prime itself, it is possible to continuously
remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

Candidate primes:
must begin with 2,3,5,7
must end with 3,7
must not have a 0
may have 2,5 only in first position

Truncatable Primes: 23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397
"""

from utils.prime import is_prime, primes


class Problem37(object):
    @staticmethod
    def solve():
        def is_truncatable_prime(p):
            if p < 10: return False
            s = str(p)
            # these optimizations make it about 2x as fast (0.22s -> 0.11s)
            if s[0] not in ('2357'): return False
            if s[-1] not in ('37'): return False
            if '0' in s: return False
            if '2' in s[1:]: return False
            if '5' in s[1:]: return False
            # check all truncations
            return all(is_prime(int(s[:-i])) and is_prime(int(s[i:])) for i in range(1, len(s)))

        # can i prove 1000000 is a good limit?
        return sum(p for p in primes(1000000) if is_truncatable_prime(p))

    @staticmethod
    def get_tests():
        return [(None, 748317)]


if __name__ == '__main__':
    print("The answer is", Problem37.solve())
