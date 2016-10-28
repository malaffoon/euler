import unittest

from utils.iter import rotations, slide


class IterTests(unittest.TestCase):
    def test_slide(self):
        self.assertEqual([(1, 2), (2, 3), (3, 4)], list(slide(range(1, 5))))
        self.assertEqual([(1, 2, 3, 4), (2, 3, 4, 5)], list(slide(range(1, 6), 4)))
        self.assertEqual(['abc', 'bcd', 'cde', 'def'], list(slide('abcdef', 3)))

    def test_rotations(self):
        self.assertEqual(('abcd', 'bcda', 'cdab', 'dabc'), tuple(rotations('abcd')))
        self.assertEqual((1234, 2341, 3412, 4123), tuple(rotations(1234)))
        self.assertEqual(('1.23', '.231', '231.', '31.2'), tuple(rotations(1.23)))  # nonsensical
        self.assertEqual(((1, 2, 3, 4), (2, 3, 4, 1), (3, 4, 1, 2), (4, 1, 2, 3)), tuple(rotations(range(1, 5))))
        self.assertEqual((('abc',),), tuple(rotations(['abc'])))


if __name__ == '__main__':
    unittest.main()
