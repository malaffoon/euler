import unittest

from problems.problem48 import Problem48


class Problem48Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual('9110846700', Problem48.solve())

    def test_example(self):
        self.assertEqual('0405071317', Problem48.solve(10))


if __name__ == '__main__':
    unittest.main()
