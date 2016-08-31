import unittest

from problems.problem21 import Problem21


class Problem21Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(31626, Problem21.solve())


if __name__ == '__main__':
    unittest.main()