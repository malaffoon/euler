import unittest

from problems.problem4 import Problem4


class Problem4Tests(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(906609, Problem4().solve())


if __name__ == '__main__':
    unittest.main()