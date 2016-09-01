import unittest

from problems.problem5 import Problem5


class Problem5Tests(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(232792560, Problem5.solve())


if __name__ == '__main__':
    unittest.main()