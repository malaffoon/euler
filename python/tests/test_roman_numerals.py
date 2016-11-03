import unittest

from utils.roman_numerals import fromRomanNumeral, toRomanNumeral


class RomanNumeralTests(unittest.TestCase):
    def test_fromRomanNumeral(self):
        self.assertEqual(1, fromRomanNumeral('I'))
        self.assertEqual(9, fromRomanNumeral('IX'))
        self.assertEqual(1964, fromRomanNumeral('MCMLXIV'))

    def test_toRomanNumeral(self):
        self.assertEqual('I', toRomanNumeral(1))
        self.assertEqual('IX', toRomanNumeral(9))
        self.assertEqual('MCMLXIV', toRomanNumeral(1964))

    def test_roundtrip(self):
        for n in range(2000):
            self.assertEqual(n, fromRomanNumeral(toRomanNumeral(n)))