import unittest
import math


class PrimeTests(unittest.TestCase):
    def test_prime_generator(self):
        from utils.prime import primes
        self.assertEqual([2], list(primes(3)))
        self.assertEqual([2,3], list(primes(4)))
        self.assertEqual([2,3,5], list(primes(6)))

    def test_prime_factors(self):
        from utils.prime import prime_factors
        self.assertEqual([2], prime_factors(2))
        self.assertEqual([3], prime_factors(3))
        self.assertEqual([17], prime_factors(17))
        self.assertEqual([2,2,3], prime_factors(12))
        self.assertEqual([5,7,13,29], prime_factors(13195))
        self.assertEqual([71,839,1471,6857], prime_factors(600851475143))

    def test_factors(self):
        from utils.prime import factors
        self.assertEqual([2], list(factors(2)))
        self.assertEqual([3], list(factors(3)))
        self.assertEqual([3,3], list(factors(9)))
        self.assertEqual([17], list(factors(17)))
        self.assertEqual([2,2,3], list(factors(12)))
        self.assertEqual([5,7,13,29], list(factors(13195)))
        self.assertEqual([71,839,1471,6857], list(factors(600851475143)))

    def test_factors_grouped(self):
        from utils.prime import factors_grouped
        self.assertEqual([(2,1)], factors_grouped(2))
        self.assertEqual([(3,1)], factors_grouped(3))
        self.assertEqual([(3,2)], factors_grouped(9))
        self.assertEqual([(17,1)], factors_grouped(17))
        self.assertEqual([(2,2),(3,1)], factors_grouped(12))
        self.assertEqual([(2,1),(5,2)], factors_grouped(50))
        self.assertEqual([(2,4),(5,4)], factors_grouped(10000))
        self.assertEqual([(5,1),(7,1),(13,1),(29,1)], factors_grouped(13195))

    def test_prime_generator_problem(self):
        from utils.prime import primes
        result = list(primes(math.ceil(math.sqrt(600851475143))))
        self.assertEqual(2, result[0])
        self.assertEqual(775121, result[-1])
        self.assertEqual(62113, len(result))

    def test_factors_to_divisors(self):
        from utils.prime import factors_to_divisors
        self.assertEqual([1, 2, 5, 10, 25, 50], sorted(list(factors_to_divisors((2, 5, 5)))))
        self.assertEqual([1, 2, 3, 6, 9, 18, 27, 54], sorted(list(factors_to_divisors((2, 3, 3, 3)))))

    def test_divisors(self):
        from utils.prime import divisors
        self.assertEqual([1,2], divisors(2))
        self.assertEqual([1,3], divisors(3))
        self.assertEqual([1,17], divisors(17))
        self.assertEqual([1,2,3,4,6,12], divisors(12))

    def test_is_prime(self):
        from utils.prime import is_prime
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(81))
        self.assertFalse(is_prime(1681))
        self.assertFalse(is_prime(10000))

        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(6857))

    def test_is_prime_some_more(self):
        from utils.prime import is_prime
        self.assertTrue(is_prime(4547337172376300111955330758342147474062293202868155909489))
        self.assertFalse(is_prime(4547337172376300111955330758342147474062293202868155909393))
        self.assertTrue(is_prime(643808006803554439230129854961492699151386107534013432918073439524138264842370630061369715394739134090922937332590384720397133335969549256322620979036686633213903952966175107096769180017646161851573147596390153))
        self.assertFalse(is_prime(743808006803554439230129854961492699151386107534013432918073439524138264842370630061369715394739134090922937332590384720397133335969549256322620979036686633213903952966175107096769180017646161851573147596390153))

    def test_phi(self):
        from utils.prime import phi
        self.assertEqual(6, phi(9))
        self.assertEqual(22, phi(23))
        self.assertEqual(8313928, phi(8319823))
        self.assertEqual(9701832, phi(9708131))

    def test_nth(self):
        from utils.prime import nth
        self.assertEqual(29, nth(10))
        self.assertEqual(541, nth(100))
        self.assertEqual(7919, nth(1000))
        self.assertEqual(104743, nth(10001))


if __name__ == '__main__':
    unittest.main()
