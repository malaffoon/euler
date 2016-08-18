import unittest

from problems.problem3 import Problem3


class Problem3Tests(unittest.TestCase):
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