import unittest

from problems.problem15 import Problem15


class Problem15Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEquals(137846528820, Problem15.solve())

    def test_examples(self):
        self.assertEquals(6, Problem15.solve(2))
        self.assertEquals(20, Problem15.solve(3))
        self.assertEquals(70, Problem15.solve(4))

    def test_solve2(self):
        self.assertEquals(6, Problem15.solve2(2))
        self.assertEquals(20, Problem15.solve2(3))
        self.assertEquals(70, Problem15.solve2(4))
        self.assertEquals(137846528820, Problem15.solve2())

if __name__ == '__main__':
    unittest.main()