import unittest
from itertools import islice

from utils.fibonacci import Fibonacci
from utils.fibonacci import fibgen
from utils.fibonacci import fibn


class FibonacciTests(unittest.TestCase):
    def test_default(self):
        self.assertEqual([1, 1, 2, 3, 5, 8, 13, 21, 34, 55], list(Fibonacci()))

    def test_max_count(self):
        self.assertEqual([1, 1, 2], list(Fibonacci(max_count=3)))

    def test_max_value(self):
        self.assertEqual([1, 1, 2, 3, 5, 8], list(Fibonacci(max_value=10)))

    def test_no_limit(self):
        self.assertRaises(ValueError, Fibonacci, max_count=None, max_value=None)

    def test_fibgen_default(self):
        self.assertEqual([1, 1, 2, 3, 5, 8, 13, 21, 34, 55], list(fibgen()))

    def test_fibgen_max_count(self):
        self.assertEqual([1, 1, 2, 3], list(fibgen(max_count=4)))

    def test_fibgen_max_value(self):
        self.assertEqual([1, 1, 2, 3, 5, 8, 13], list(fibgen(max_value=15)))

    def test_fibn(self):
        self.assertEqual(1, fibn(1))
        self.assertEqual(1, fibn(2))
        self.assertEqual(13, fibn(7))
        self.assertEqual(3524578, fibn(33))

if __name__ == '__main__':
    unittest.main()
