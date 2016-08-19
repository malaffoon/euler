import unittest

from problems.problem5 import Problem5, least_common_multiple


class Problem5Tests(unittest.TestCase):
    def test_least_common_multiple(self):
        self.assertEqual(1, least_common_multiple([1]))
        self.assertEqual(7, least_common_multiple([7]))
        self.assertEqual(1, least_common_multiple([1,1,1]))
        self.assertEqual(2, least_common_multiple([1,2]))
        self.assertEqual(72, least_common_multiple([8,9,12]))
        self.assertEqual(1207, least_common_multiple([17,71]))
        self.assertEqual(2520, least_common_multiple(range(1,10)))

    def test_solution(self):
        self.assertEqual(232792560, Problem5().solve())


if __name__ == '__main__':
    unittest.main()