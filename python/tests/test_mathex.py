import unittest

import itertools
import utils.mathex as m


class MathTests(unittest.TestCase):
    def test_lcm(self):
        self.assertEqual(1, m.lcm([1]))
        self.assertEqual(7, m.lcm([7]))
        self.assertEqual(1, m.lcm([1, 1, 1]))
        self.assertEqual(2, m.lcm([1, 2]))
        self.assertEqual(72, m.lcm([8, 9, 12]))
        self.assertEqual(1207, m.lcm([17, 71]))
        self.assertEqual(2520, m.lcm(range(1, 10)))

    def test_champerone(self):
        self.assertEqual([1, 2, 3], list(itertools.islice(m.champernowne(), 0, 3)))
        self.assertEqual([1, 1, 2, 1, 3, 1], list(itertools.islice(m.champernowne(), 12, 18)))

    def test_digits(self):
        self.assertEqual([3, 3, 2, 1], list(m.digits(1233)))
        self.assertEqual([0, 9], list(m.digits(90)))

    def test_is_pandigital(self):
        self.assertTrue(m.is_pandigital(231))
        self.assertTrue(m.is_pandigital('918273645'))
        self.assertFalse(m.is_pandigital(1233))
        self.assertFalse(m.is_pandigital('91827'))

    def test_trigonal(self):
        self.assertEqual([1, 3, 6, 10, 15], list(m.trigonal(n) for n in range(1, 6)))
        self.assertEqual([4, None, None, None, None, 5, None, None, None, None],
                         list(m.is_trigonal(v) for v in range(10, 20)))

    def test_tetragonal(self):
        self.assertEqual([1, 4, 9, 16, 25], list(m.tetragonal(n) for n in range(1, 6)))
        self.assertEqual([3, None, None, None, None, None, None, 4, None],
                         list(m.is_tetragonal(v) for v in range(9, 18)))

    def test_pentagonal(self):
        self.assertEqual([1, 5, 12, 22, 35], list(m.pentagonal(n) for n in range(1, 6)))
        self.assertEqual([2, None, None, None, None, None, None, 3, None],
                         list(m.is_pentagonal(v) for v in range(5, 14)))

    def test_hexagonal(self):
        self.assertEqual([1, 6, 15, 28, 45], list(m.hexagonal(n) for n in range(1, 6)))
        self.assertEqual([1, None, None, None, None, 2, None],
                         list(m.is_hexagonal(v) for v in range(1, 8)))

    def test_heptagonal(self):
        self.assertEqual([1, 7, 18, 34, 55], list(m.heptagonal(n) for n in range(1, 6)))
        self.assertEqual(2, m.is_heptagonal(7))
        self.assertEqual(None, m.is_heptagonal(10))

    def test_octagonal(self):
        self.assertEqual([1, 8, 21, 40, 65], list(m.octagonal(n) for n in range(1, 6)))
        self.assertEqual(2, m.is_octagonal(8))
        self.assertEqual(None, m.is_octagonal(10))

    def test_tripenthex_example(self):
        self.assertEqual(285, m.is_trigonal(40755))
        self.assertEqual(165, m.is_pentagonal(40755))
        self.assertEqual(143, m.is_hexagonal(40755))

    def test_isqrt(self):
        self.assertEqual(10, m.isqrt(100))
        self.assertEqual(169, m.isqrt(28561))
        self.assertEqual(28561, m.isqrt(815730721))
        self.assertEqual(815730721, m.isqrt(665416609183179841))
        self.assertEqual(665416609183179841, m.isqrt(442779263776840698304313192148785281))
        self.assertEqual(10, m.isqrt(110))
        self.assertEqual(169, m.isqrt(28600))

    def test_pell(self):
        self.assertEqual([(2, 1), (7, 4), (26, 15), (97, 56)],
                         list(itertools.takewhile(lambda p: p[0] < 100, m.pell_gen(3))))
        self.assertEqual([(8, 3), (127, 48), (2024, 765)],
                         list(itertools.takewhile(lambda p: p[0] < 10000, m.pell_gen(7))))


if __name__ == '__main__':
    unittest.main()
