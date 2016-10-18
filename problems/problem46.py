"""Problem 46 - Project Euler

Goldbach's other conjecture

It was proposed by Christian Goldbach that every odd composite number can be written
as the sum of a prime and twice a square.

  | 9 = 7 + 2×12
  | 15 = 7 + 2×22
  | 21 = 3 + 2×32
  | 25 = 7 + 2×32
  | 27 = 19 + 2×22
  | 33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
from itertools import count

from utils.prime import is_prime


class Problem46(object):
    @staticmethod
    def solve():
        twice_squares = list(2 * i * i for i in range(1, 100))
        for n in count(35, 2):
            if is_prime(n): continue
            # it is 30x faster to go through squares than to go through primes; 50ms vs 1.3s
            # if any((n-p) in twice_squares for p in primes(n)): continue
            if any(is_prime(n - ts) for ts in twice_squares if ts < n): continue
            return n

    @staticmethod
    def get_tests():
        return [(None, 5777)]


if __name__ == '__main__':
    print("The answer is", Problem46.solve())
