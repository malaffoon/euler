import unittest

from problems.problem32 import Problem32


class Problem32Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(45228, Problem32.solve())


if __name__ == '__main__':
    unittest.main()