import unittest

from utils import collatz
from problems.problem14 import Problem14


class Problem14Tests(unittest.TestCase):
    def test_solve(self):
        result = Problem14.solve()
        self.assertEquals(837799, result)
        self.assertEquals(525, sum(1 for _ in collatz.generator(result)))


if __name__ == '__main__':
    unittest.main()