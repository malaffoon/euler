import unittest

from problems.problem18 import Problem18, PROBLEM18_EXAMPLE


class Problem18Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(1074, Problem18.solve())

    def test_example(self):
        self.assertEqual(23, Problem18.solve(PROBLEM18_EXAMPLE))


if __name__ == '__main__':
    unittest.main()