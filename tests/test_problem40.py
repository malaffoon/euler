import unittest

from problems.problem40 import Problem40


class Problem40Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(210, Problem40.solve())


if __name__ == '__main__':
    unittest.main()
