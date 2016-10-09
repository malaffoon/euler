import unittest

from problems.problem79 import Problem79


class Problem79Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual('73162890', Problem79.solve())


if __name__ == '__main__':
    unittest.main()