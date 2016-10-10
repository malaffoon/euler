import unittest

from problems.problem89 import Problem89


class Problem89Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(743, Problem89.solve())


if __name__ == '__main__':
    unittest.main()