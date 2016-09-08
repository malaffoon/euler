import unittest

from problems.problem26 import Problem26


class Problem26Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(983, Problem26.solve())

    def test_example(self):
        self.assertEqual(7, Problem26.solve(10))
        self.assertEqual(97, Problem26.solve(100))


if __name__ == '__main__':
    unittest.main()