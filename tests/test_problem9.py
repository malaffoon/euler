import unittest

from problems.problem9 import Problem9


class Problem8Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEquals(31875000, Problem9.solve())

    def test_example(self):
        self.assertEqual(60, Problem9.solve(12))


if __name__ == '__main__':
    unittest.main()