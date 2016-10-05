import unittest

from problems.problem47 import Problem47


class Problem47Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(134043, Problem47.solve())

    def test_example(self):
        self.assertEqual(14, Problem47.solve(2))
        self.assertEqual(644, Problem47.solve(3))


if __name__ == '__main__':
    unittest.main()
