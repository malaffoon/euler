import unittest

from problems.problem29 import Problem29


class Problem29Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(9183, Problem29.solve())

    def test_example(self):
        self.assertEqual(15, Problem29.solve(5))


if __name__ == '__main__':
    unittest.main()