import unittest

from problems.problem38 import Problem38


class Problem38Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(932718654, Problem38.solve())

    def test_concatenated_product(self):
        self.assertEqual('192384576', Problem38.__concatenated_product__(192, (1, 2, 3)))
        self.assertEqual('918273645', Problem38.__concatenated_product__(9, (1, 2, 3, 4, 5)))


if __name__ == '__main__':
    unittest.main()