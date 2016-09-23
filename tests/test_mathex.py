import unittest

import itertools
from utils.mathex import lcm, champernowne


class MathTests(unittest.TestCase):
    def test_lcm(self):
        self.assertEqual(1, lcm([1]))
        self.assertEqual(7, lcm([7]))
        self.assertEqual(1, lcm([1, 1, 1]))
        self.assertEqual(2, lcm([1, 2]))
        self.assertEqual(72, lcm([8, 9, 12]))
        self.assertEqual(1207, lcm([17, 71]))
        self.assertEqual(2520, lcm(range(1, 10)))

    def test_champerone(self):
        self.assertEqual([1, 2, 3], list(itertools.islice(champernowne(), 0, 3)))
        self.assertEqual([1, 1, 2, 1, 3, 1], list(itertools.islice(champernowne(), 12, 18)))


if __name__ == '__main__':
    unittest.main()
