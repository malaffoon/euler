import cProfile

from utils.prime import primes, rabin_primes, atkin_primes

"""
  limit    primes  reflective  rabin    atkin
  20000    0.005      0.74     0.19    0.083
 200000    0.055     44.       1.9     2.1
2000000    0.60        -      18.     53.
"""

if __name__ == '__main__':
    cProfile.run('list(primes(20000))')
    cProfile.run('list(reflective_primes(20000))')
    cProfile.run('list(rabin_primes(20000))')
    cProfile.run('list(atkin_primes(20000))')


