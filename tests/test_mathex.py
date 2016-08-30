import unittest

from utils.mathex import lcm


class MathTests(unittest.TestCase):
    def test_lcm(self):
        self.assertEqual(1, lcm([1]))
        self.assertEqual(7, lcm([7]))
        self.assertEqual(1, lcm([1, 1, 1]))
        self.assertEqual(2, lcm([1, 2]))
        self.assertEqual(72, lcm([8, 9, 12]))
        self.assertEqual(1207, lcm([17, 71]))
        self.assertEqual(2520, lcm(range(1, 10)))

if __name__ == '__main__':
    unittest.main()
