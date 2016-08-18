import unittest

from problems.problem4 import Problem4, is_palindrome


class Problem4Tests(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertEqual(True, is_palindrome(0))
        self.assertEqual(True, is_palindrome(5))
        self.assertEqual(True, is_palindrome(22))
        self.assertEqual(True, is_palindrome(101))
        self.assertEqual(True, is_palindrome(1234321))
        self.assertEqual(True, is_palindrome(12344321))
        self.assertEqual(False, is_palindrome(10))
        self.assertEqual(False, is_palindrome(102))
        self.assertEqual(False, is_palindrome(1234322))

        self.assertEqual(False, is_palindrome("Bob"))
        self.assertEqual(True, is_palindrome("bob"))

    def test_solution(self):
        self.assertEqual(906609, Problem4().solve())


if __name__ == '__main__':
    unittest.main()