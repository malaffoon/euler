import unittest

from problems.problem1 import Problem1


class Problem1Tests(unittest.TestCase):
    def test_example(self):
        self.assertEqual(23, Problem1().solve(10))

    def test_solution(self):
        self.assertEqual(233168, Problem1().solve(1000))

if __name__ == '__main__':
    unittest.main()