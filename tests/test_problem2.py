import unittest

from problems.problem2 import Problem2


class Problem2Tests(unittest.TestCase):
    def test_example(self):
        self.assertEqual(44, Problem2().solve(100))

    def test_solution(self):
        self.assertEqual(4613732, Problem2().solve())

if __name__ == '__main__':
    unittest.main()