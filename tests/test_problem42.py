import unittest

from problems.problem42 import Problem42


class Problem42Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(162, Problem42.solve())


if __name__ == '__main__':
    unittest.main()
