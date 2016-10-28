import unittest

from problems.problem24 import Problem24


class Problem24Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual('2783915460', Problem24.solve())

    def test_example(self):
        self.assertEqual('102', Problem24.solve(range(0, 3), 3))


if __name__ == '__main__':
    unittest.main()