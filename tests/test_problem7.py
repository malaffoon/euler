import unittest

from problems.problem7 import Problem7


class Problem7Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEquals(2, Problem7.solve(1))
        self.assertEquals(29, Problem7.solve(10))
        self.assertEquals(541, Problem7.solve(100))
        self.assertEquals(7919, Problem7.solve(1000))

    def test_example(self):
        self.assertEqual(13, Problem7().solve(6))

    def test_solution(self):
        self.assertEqual(104743, Problem7().solve())


if __name__ == '__main__':
    unittest.main()