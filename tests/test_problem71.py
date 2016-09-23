import unittest

from problems.problem71 import Problem71


class Problem71Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(428570, Problem71.solve())

    def test_example(self):
        self.assertEqual(2, Problem71.solve(8))
        self.assertEqual(2, Problem71.solve_loop(8))
        self.assertEqual(2, Problem71.solve_list(8))

        self.assertEqual(41, Problem71.solve(100))
        self.assertEqual(41, Problem71.solve_loop(100))
        self.assertEqual(41, Problem71.solve_list(100))

        self.assertEqual(428, Problem71.solve(1000))
        self.assertEqual(428, Problem71.solve_loop(1000))
        self.assertEqual(428, Problem71.solve_list(1000))


if __name__ == '__main__':
    unittest.main()