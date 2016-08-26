import unittest

from problems.problem13 import Problem13


class Problem13Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEquals('5537376230', Problem13.solve())


if __name__ == '__main__':
    unittest.main()