import cProfile

from utils.prime import divisors, factors, phi, primes, is_prime, prime_factors, factors_grouped, nth

# for sieve of eratosthenes: primes(2000000) takes a bit less than 0.6s

if __name__ == '__main__':
    cProfile.run('list(primes(2000000))')

