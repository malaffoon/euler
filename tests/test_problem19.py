import unittest

from problems.problem19 import Problem19


class Problem19Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(171, Problem19.solve())

    def test_solve2(self):
        self.assertEqual(171, Problem19.solve2())


if __name__ == '__main__':
    unittest.main()