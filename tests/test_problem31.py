import unittest

from problems.problem31 import Problem31


class Problem31Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(73682, Problem31.solve())


if __name__ == '__main__':
    unittest.main()