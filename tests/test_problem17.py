import unittest

from problems.problem17 import Problem17, letters, words


class Problem17Tests(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(21124, Problem17.solve())

    def test_example(self):
        self.assertEqual(19, Problem17.solve(5))

    def test_words(self):
        self.assertEqual('three hundred and forty two', words(342))
        self.assertEqual('one hundred and fifteen', words(115))

    def test_letters(self):
        self.assertEqual(23, letters(words(342)))
        self.assertEqual(20, letters(words(115)))

if __name__ == '__main__':
    unittest.main()