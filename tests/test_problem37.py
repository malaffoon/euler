import unittest

from problems.problem37 import Problem37


class Problem37Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(748317, Problem37.solve())


if __name__ == '__main__':
    unittest.main()