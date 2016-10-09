import unittest

from problems.problem65 import Problem65


class Problem65Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(272, Problem65.solve())

    def test_example(self):
        self.assertEqual(17, Problem65.solve(10))


if __name__ == '__main__':
    unittest.main()