import unittest

from problems.problem41 import Problem41


class Problem41Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(7652413, Problem41.solve())


if __name__ == '__main__':
    unittest.main()
