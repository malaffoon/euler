import unittest

from problems.problem50 import Problem50


class Problem50Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(997651, Problem50.solve())

    def test_example(self):
        self.assertEqual(41, Problem50.solve(100))
        self.assertEqual(953, Problem50.solve(1000))


if __name__ == '__main__':
    unittest.main()