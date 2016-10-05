import unittest

from utils.iter import slide


class IterTests(unittest.TestCase):
    def test_slide(self):
        self.assertEqual([(1, 2), (2, 3), (3, 4)], list(slide(range(1, 5))))


if __name__ == '__main__':
    unittest.main()
