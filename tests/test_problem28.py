import unittest

from problems.problem28 import Problem28


class Problem28Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(669171001, Problem28.solve())

    def test_example(self):
        self.assertEqual(101, Problem28.solve(5))


if __name__ == '__main__':
    unittest.main()