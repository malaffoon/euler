import unittest

from problems.problem35 import Problem35


class Problem35Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(55, Problem35.solve())

    def test_example(self):
        self.assertEqual(13, Problem35.solve(100))


if __name__ == '__main__':
    unittest.main()