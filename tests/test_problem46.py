import unittest

from problems.problem46 import Problem46


class Problem46Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(5777, Problem46.solve())


if __name__ == '__main__':
    unittest.main()
