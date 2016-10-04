import unittest

from problems.problem45 import Problem45


class Problem45Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(1533776805, Problem45.solve())


if __name__ == '__main__':
    unittest.main()
