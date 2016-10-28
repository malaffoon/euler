import unittest

from problems.problem22 import Problem22, score


class Problem22Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(871198282, Problem22.solve())

    def test_score(self):
        self.assertEqual(49714, score(938, 'COLIN'))


if __name__ == '__main__':
    unittest.main()