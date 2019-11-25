""" Problem 357 - Project Euler

Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d + 30/d is prime.

Find the sum of all positive integers n not exceeding 100 000 000
such that for every divisor d of n, d + n/d is prime.
"""
import operator
import cProfile
import timeit

from itertools import combinations
from functools import reduce
from utils import prime


class Problem357(object):
    @staticmethod
    def solve(max_n=100000000):
        """Solve problem 357

        :param max_n: limit, defaults to problem value: 100,000,000
        :return: sum of numbers adhering to problem rules
        """
        return Problem357.solve3(max_n)

    @staticmethod
    def solve3(max_n):
        """Since max_n is relatively small, perhaps we should just generate
        all primes up to max_n, then use the rules (4x+2, n+1 must be prime,
        etc.) to filter down the list.

        Also replaced the generator with the prime sieve array.

        This approach still takes ~5m to solve.

        :param max_n:
        :return:
        """
        prime_sieve = prime.prime_sieve(max_n+1)

        def _factors(n):
            from math import sqrt
            factors = []
            for p in range(2, int(1+sqrt(n))):
                if not prime_sieve[p]: continue
                while n > 1 and n % p == 0:
                    factors.append(p)
                    n //= p
                if n == 1 or n <= p*p: break
            if n > 1:
                factors.append(n)
            return factors

        sum = 1
        for p in range(2, max_n+1):
            if not prime_sieve[p]: continue
            n = p - 1

            # n = 4x + 2
            if (n-2) % 4 != 0: continue

            # singular prime factors
            factor_list = _factors(n)
            if len(factor_list) > len(set(factor_list)): continue

            # no more short cuts, time to do the work
            divs = list(prime.factors_to_divisors(factor_list))
            len_divs = len(divs)
            # we only have to check the first half of the divisors since d+n/d is symmetric
            if all(prime_sieve[d + n // d] for d in divs[:len_divs//2]):
                sum += n
        return sum

    @staticmethod
    def solve2(max_n):
        """Reverse the strategy: generate numbers from the prime numbers up to
        sum function of max_n. Combine them using singular occurrences.
        - 2 is always a factor
        - n+1 must be prime
        This approach requires less filtering: we know we are getting even
        numbers that aren't prime and aren't perfect squares. The only tricky
        bit is knowing when to stop looking, i.e. how big should c get? And i
        don't have a solution for that so this isn't tenable ...

        This approach never finished solving.

        :param max_n:
        :return:
        """
        # get all primes up to square root of max value
        # prime_list = list(prime.primes(int(math.sqrt(max_n))))[1:]
        prime_list = list(prime.primes(max_n//2))[1:]

        sum = 3   # 1 + 2
        for c in range(1, 5):
            for combo in combinations(prime_list, c):
                factors = (2,) + combo
                n = reduce(operator.mul, factors, 1)
                if n > max_n: continue

                # TODO - we need a way to skip bits

                # okay, check the number
                divs = sorted(list(prime.factors_to_divisors(factors)))
                if all(prime.is_prime(d + n // d) for d in divs[:len(divs)//2]):
                    sum += n
                    print(n, factors, divs)
        return sum

    @staticmethod
    def solve1(max_n):
        """This was the initial (naive) approach: go through all the numbers in
        the range and check the condition for all divisors. There are a couple
        optimizations:
        - n+1 must be prime => only consider even numbers
        - further fiddling shows n = 4x + 2, so we can actually jump by 4 instead of 2
        - perfect squares (n=s*s) will never match because s+n/s = 2s which is not prime
        - extending the previous point, only consider numbers with singular prime factors
        - d+n/d is symmetric across divisors so only half to check first half of divisors
        Still, it takes 10m to solve for 100,000,000.

        :param max_n:
        :return:
        """
        sum = 3   # 1 + 2
        for n in range(6, max_n+1, 4):
            # some quick checks to eliminate numbers
            # we're already considering just even numbers

            # d+n/d must be odd for d=2
            if n//2 % 2 == 0: continue

            # n+1 must be prime
            if not prime.is_prime(n+1): continue

            # prime factors must be singular (or else d+n/d would be a multiple of d, i.e. not prime)
            factor_list = list(prime.factors(n))
            if len(factor_list) > len(set(factor_list)): continue

            # no more short cuts, time to do the work
            divs = list(prime.factors_to_divisors(factor_list))
            len_divs = len(divs)
            # primes and perfect squares won't match
            if len_divs > 2 and len_divs % 2 == 0:
                # we only have to check the first half of the divisors since d+n/d is symmetric
                if all(prime.is_prime(d + n // d) for d in divs[:len_divs//2]):
                    sum += n
        return sum

    @staticmethod
    def get_tests():
        # it takes 6-7m to solve for 100000000 so leave that out of the automatic tests
        # return [(100000000, 1739023853137), (10000, 262615), (100000, 9157937)]
        return [(10000, 262615), (100000, 9157937)]


if __name__ == '__main__':
    # cProfile.run('Problem357.solve3(1000000)')
    # print(timeit.timeit('Problem357().solve3(100000000)', setup='from problems.problem357 import Problem357', number=1))
    print("The answer is", Problem357.solve(100000))
