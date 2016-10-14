import unittest

from problems.problem51 import Problem51


class Problem51Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(121313, Problem51.solve())

    def test_example(self):
        self.assertEqual(13, Problem51.solve(6))
        self.assertEqual(56003, Problem51.solve(7))


if __name__ == '__main__':
    unittest.main()