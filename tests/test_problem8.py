import unittest

from problems.problem8 import Problem8


class Problem8Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEquals(23514624000, Problem8.solve())

    def test_example(self):
        self.assertEqual(5832, Problem8().solve(4))


if __name__ == '__main__':
    unittest.main()