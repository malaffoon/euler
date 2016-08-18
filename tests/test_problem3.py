import unittest
import math

from problems.problem3 import Problem3, primegen, prime_factors


class Problem3Tests(unittest.TestCase):
    def test_primegen(self):
        self.assertEqual([2], list(primegen(3)))
        self.assertEqual([2,3], list(primegen(4)))
        self.assertEqual([2,3,5], list(primegen(6)))

    def test_prime_factors(self):
        self.assertEqual([2], prime_factors(2))
        self.assertEqual([3], prime_factors(3))
        self.assertEqual([17], prime_factors(17))
        self.assertEqual([2,2,3], prime_factors(12))
        self.assertEqual([5,7,13,29], prime_factors(13195))
        self.assertEqual([71,839,1471,6857], prime_factors(600851475143))

    def test_primegen_problem(self):
        result = list(primegen(math.ceil(math.sqrt(600851475143))))
        self.assertEqual(2, result[0])
        self.assertEqual(775121, result[-1])
        self.assertEqual(62113, len(result))

    def test_example(self):
        self.assertEqual(29, Problem3().solve(13195))

    def test_one(self):
        self.assertEquals(1, Problem3.solve(1))

    def test_three(self):
        self.assertEquals(3, Problem3.solve(3))

    def test_prime(self):
        self.assertEquals(13147, Problem3.solve(13147))

    def test_solution(self):
        self.assertEqual(6857, Problem3().solve(600851475143))


if __name__ == '__main__':
    unittest.main()