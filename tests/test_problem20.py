import unittest

from problems.problem20 import Problem20


class Problem20Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(648, Problem20.solve())

    def test_example(self):
        self.assertEqual(27, Problem20.solve(10))


if __name__ == '__main__':
    unittest.main()