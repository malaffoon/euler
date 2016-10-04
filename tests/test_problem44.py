import unittest

from problems.problem44 import Problem44


class Problem44Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(5482660, Problem44.solve())


if __name__ == '__main__':
    unittest.main()
