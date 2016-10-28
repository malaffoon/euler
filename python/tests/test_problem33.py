import unittest

from problems.problem33 import Problem33


class Problem33Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(100, Problem33.solve())

    def test_digit_cancelled(self):
        self.assertIsNone(Problem33.digit_cancelled(30, 50))
        self.assertIsNone(Problem33.digit_cancelled(45, 54))
        self.assertIsNone(Problem33.digit_cancelled(77, 77))
        self.assertIsNone(Problem33.digit_cancelled(37, 84))
        self.assertIsNone(Problem33.digit_cancelled(15, 50))
        self.assertEqual(0.5, Problem33.digit_cancelled(49, 98))


if __name__ == '__main__':
    unittest.main()