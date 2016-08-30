import unittest

from problems.problem49 import Problem49


class Problem49Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual('296962999629', Problem49.solve())


if __name__ == '__main__':
    unittest.main()