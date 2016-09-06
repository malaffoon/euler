import unittest

from problems.problem30 import Problem30


class Problem30Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(443839, Problem30.solve())

    def test_example(self):
        self.assertEqual(19316, Problem30.solve(4))


if __name__ == '__main__':
    unittest.main()