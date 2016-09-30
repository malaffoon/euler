import unittest

from problems.problem92 import Problem92


class Problem92Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(8581146, Problem92.solve())


if __name__ == '__main__':
    unittest.main()
