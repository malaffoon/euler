"""Problem 42 - Project Euler

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
  | 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding
these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""


class Problem42(object):
    @staticmethod
    def solve():
        TRIANGLE_NUMBERS = [n*(n+1)//2 for n in range(1, 30)]

        def word_value(word):
            return sum(ord(c) - ord('A') + 1 for c in word)

        def read_words():
            with open('../resources/p042_words.txt') as file:
                return (s.strip('"') for s in file.read().split(','))

        return sum(1 for _ in filter(lambda v: v in TRIANGLE_NUMBERS, (word_value(w) for w in read_words())))


if __name__ == '__main__':
    print("The answer is", Problem42.solve())
