import unittest

from problems.problem39 import Problem39


class Problem39Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(840, Problem39.solve())


if __name__ == '__main__':
    unittest.main()