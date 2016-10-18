""" Problem 17 - Project Euler

    Number letter counts

    If the numbers 1 to 5 are written out in words: one, two, three, four, five,
    then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
    how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters
    and 115 (one hundred and fifteen) contains 20 letters.
    The use of "and" when writing out numbers is in compliance with British usage.
"""

NUMBERS = [None, 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
           'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
TENS = [None, None, 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


class Problem17(object):
    @staticmethod
    def solve(n=1000):
        return sum(letters(words(n)) for n in range(1, n+1))

    @staticmethod
    def get_tests():
        return [(1000, 21124), (5, 19)]


def letters(s):
    """Return number of non-space letters in a string"""
    return sum(1 for _ in filter(lambda c: c != ' ', s))


def words(n):
    """Express a number in british words

       For example
          342 -> "three hundred and forty two"
    """
    if n < 1 or n > 1000:
        raise ValueError('words only handles numbers from 1 to 1000')

    if n < 20:
        return NUMBERS[n]
    if n < 100:
        return ' '.join(filter(None, [TENS[n//10], NUMBERS[n%10]]))
    if n < 1000:
        result = NUMBERS[n//100] + ' hundred'
        if n%100 != 0:
            result = result + ' and ' + words(n%100)
        return result
    if n == 1000:
        return "one thousand"


if __name__ == '__main__':
    print("The number of letters used to write out the numbers from 1 to 1000 is", Problem17().solve())
