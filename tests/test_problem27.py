import unittest

from problems.problem27 import Problem27


class Problem27Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(-59231, Problem27.solve())

    def test_example(self):
        self.assertEqual(40, Problem27.number_of_primes_for(1, 41))
        self.assertEqual(80, Problem27.number_of_primes_for(-79, 1601))


if __name__ == '__main__':
    unittest.main()