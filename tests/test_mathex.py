import unittest

import itertools
from utils.mathex import lcm, champernowne, digits, is_pandigital, triagonal, is_triagonal, pentagonal, is_pentagonal, \
    hexagonal, is_hexagonal


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

    def test_digits(self):
        self.assertEqual([3, 3, 2, 1], list(digits(1233)))
        self.assertEqual([0, 9], list(digits(90)))

    def test_is_pandigital(self):
        self.assertTrue(is_pandigital(231))
        self.assertTrue(is_pandigital('918273645'))
        self.assertFalse(is_pandigital(1233))
        self.assertFalse(is_pandigital('91827'))

    def test_triagonal(self):
        self.assertEqual([1, 3, 6, 10, 15], list(triagonal(n) for n in range(1, 6)))
        self.assertEqual([4, None, None, None, None, 5, None, None, None, None],
                         list(is_triagonal(v) for v in range(10, 20)))

    def test_pentagonal(self):
        self.assertEqual([1, 5, 12, 22, 35], list(pentagonal(n) for n in range(1, 6)))
        self.assertEqual([2, None, None, None, None, None, None, 3, None],
                         list(is_pentagonal(v) for v in range(5, 14)))

    def test_hexagonal(self):
        self.assertEqual([1, 6, 15, 28, 45], list(hexagonal(n) for n in range(1, 6)))
        self.assertEqual([1, None, None, None, None, 2, None],
                         list(is_hexagonal(v) for v in range(1, 8)))

    def test_tripenthex_example(self):
        self.assertEqual(285, is_triagonal(40755))
        self.assertEqual(165, is_pentagonal(40755))
        self.assertEqual(143, is_hexagonal(40755))


if __name__ == '__main__':
    unittest.main()
