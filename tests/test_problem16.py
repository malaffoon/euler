import unittest

from problems.problem16 import Problem16


class Problem16Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(1366, Problem16.solve())

    def test_example(self):
        self.assertEqual(5, Problem16.solve(5))
        self.assertEqual(26, Problem16.solve(15))

if __name__ == '__main__':
    unittest.main()