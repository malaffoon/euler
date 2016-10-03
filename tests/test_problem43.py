import unittest

from problems.problem43 import Problem43


class Problem43Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(16695334890, Problem43.solve())


if __name__ == '__main__':
    unittest.main()
