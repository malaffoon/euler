import unittest

from problems.problem55 import Problem55


class Problem55Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(249, Problem55.solve())


if __name__ == '__main__':
    unittest.main()