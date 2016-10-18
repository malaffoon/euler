import unittest

from problems.problem17 import letters, words


class Problem17Tests(unittest.TestCase):
    def test_words(self):
        self.assertEqual('three hundred and forty two', words(342))
        self.assertEqual('one hundred and fifteen', words(115))

    def test_letters(self):
        self.assertEqual(23, letters(words(342)))
        self.assertEqual(20, letters(words(115)))

if __name__ == '__main__':
    unittest.main()