"""Problem 3 - Project Euler

   Largest prime factor

   The prime factors of 13195 are 5, 7, 13 and 29.

   What is the largest prime factor of the number 600851475143 ?
"""

from utils.prime import prime_factors


class Problem3(object):
    @staticmethod
    def solve(value):
        """Return the largest prime factor of the value"""
        return prime_factors(value)[-1]

    @staticmethod
    def get_tests():
        return [(600851475143, 6857), (13147, 13147), (3, 3), (1, 1), (13195, 29)]


if __name__ == '__main__':
    print("The largest prime factor of the number 600851475143 is", Problem3().solve(600851475143))
    print("The prime factors are", prime_factors(600851475143))
