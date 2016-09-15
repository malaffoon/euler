import unittest

from problems.problem36 import Problem36


class Problem36Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(872187, Problem36.solve())

    def test_example(self):
        # 1,3,5,7,9
        self.assertEqual(25, Problem36.solve(10))


if __name__ == '__main__':
    unittest.main()