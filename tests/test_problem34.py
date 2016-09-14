import unittest

from problems.problem34 import Problem34


class Problem34Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(40730, Problem34.solve())

    def test_example(self):
        self.assertEqual(145, Problem34.solve(200))


if __name__ == '__main__':
    unittest.main()