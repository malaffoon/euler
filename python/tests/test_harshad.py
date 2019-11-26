import unittest

from utils.harshad import is_harshad, is_strong_harshad, is_right_truncatable_harshad


class HarshadTests(unittest.TestCase):
    def test_is_harshad(self):
        self.assertTrue(is_harshad(201))

    def test_is_strong_harshad(self):
        self.assertTrue(is_strong_harshad(201))

    def test_is_right_truncatable_harshad(self):
        self.assertTrue(is_right_truncatable_harshad(201))

    def test_problem_numbers(self):
        self.assertEqual([18,21,27,42,45,63,84,201,207,209,247,402,407,423,481,603,801,803,804,846],
                         [n for n in range(1, 1000) if is_strong_harshad(n) and is_right_truncatable_harshad(n)])


if __name__ == '__main__':
    unittest.main()
    # print(timeit.timeit('test()', setup='from __main__ import test', number=100))


