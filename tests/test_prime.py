import unittest
import math

from utils.prime import generator, prime_factors


class PrimeTests(unittest.TestCase):
    def test_prime_generator(self):
        self.assertEqual([2], list(generator(3)))
        self.assertEqual([2,3], list(generator(4)))
        self.assertEqual([2,3,5], list(generator(6)))

    def test_prime_factors(self):
        self.assertEqual([2], prime_factors(2))
        self.assertEqual([3], prime_factors(3))
        self.assertEqual([17], prime_factors(17))
        self.assertEqual([2,2,3], prime_factors(12))
        self.assertEqual([5,7,13,29], prime_factors(13195))
        self.assertEqual([71,839,1471,6857], prime_factors(600851475143))

    def test_prime_generator_problem(self):
        result = list(generator(math.ceil(math.sqrt(600851475143))))
        self.assertEqual(2, result[0])
        self.assertEqual(775121, result[-1])
        self.assertEqual(62113, len(result))

if __name__ == '__main__':
    unittest.main()