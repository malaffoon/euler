import unittest

from problems.problem23 import Problem23


class Problem23Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(4179871, Problem23.solve())


if __name__ == '__main__':
    unittest.main()