"""Problem 3 - Project Euler

   Largest prime factor

   The prime factors of 13195 are 5, 7, 13 and 29.

   What is the largest prime factor of the number 600851475143 ?
"""
import math



class Problem3(object):
    @staticmethod
    def solve(value):
        """Return the largest prime factor of the value"""
        return prime_factors(value)[-1]


def prime_factors(value):
    """Return a list of the prime factors of the value
       If the value is prime, a list of the single value will be returned
    """
    if value <= 3:
        return [value]

    factors = []

    # loop this way to avoid calculating all the primes up to sqrt if not necessary
    for prime in primegen(math.ceil(math.sqrt(value))):
        while value > 1 and value % prime == 0:
            factors.append(prime)
            value /= prime
        if value == 1:
            break
    if value > 1:
        factors.append(value)

    return factors


def primegen(limit):
    """Generate primes less than limit"""
    e = [True] * limit
    e[0] = e[1] = False
    for (i, flag) in enumerate(e):
        if flag:
            yield i
            for n in range(i*i, limit, i):
                e[n] = False

if __name__ == '__main__':
    print("The largest prime factor of the number 600851475143 is", Problem3().solve(600851475143))
    print("Prime factors are", prime_factors(600851475143))
