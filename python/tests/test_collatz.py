import unittest

from utils.collatz import generator, reverse


class CollatzTests(unittest.TestCase):
    def test_generator(self):
        self.assertEqual([1], list(generator(1)))
        self.assertEqual([2, 1], list(generator(2)))
        self.assertEqual([4, 2, 1], list(generator(4)))
        self.assertEqual([8, 4, 2, 1], list(generator(8)))
        self.assertEqual([16, 8, 4, 2, 1], list(generator(16)))

    def test_reverse(self):
        self.assertEqual(5, len(reverse(6)))
        self.assertEqual(21, len(reverse(10)))
        self.assertEqual(450, len(reverse(20)))
        self.assertEqual(7935, len(reverse(30)))
        # self.assertEqual(2461388, len(reverse(50)))


if __name__ == '__main__':
    unittest.main()