"""Problem 98 - Project Euler

Anagramic squares

By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square
number: 1296 = 362. What is remarkable is that, by using the same digital substitutions, the anagram,
RACE, also forms a square number: 9216 = 962. We shall call CARE (and RACE) a square anagram word pair
and specify further that leading zeroes are not permitted, neither may a different letter have the
same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand
common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be
an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.

---------------------------------------------------------------------------------------------------
I think we need to extract the anagram pairs from the list of words (there are 1786 words).

Turns out there are 44 anagram pairs. Longest is 9 characters.

Generate a list of square numbers, from 2 digits to 9 digits. 9 digits = 999999999. Hmm, that's
a lot (31600+). Let's do it JIT to avoid if possible.

For each pair, do substitution to match square numbers of equal length. If that is possible then
check that the other word of the pair, with the same substitution is also a square number.
"""
from itertools import combinations
import math


class Problem98(object):
    @staticmethod
    def solve():
        def read_words():
            with open('../../resources/p098_words.txt') as file:
                return (s.strip('"') for s in file.read().split(','))

        def extract_anagrams():
            words_by_length = {}    # map of length -> set of words
            for word, length in ((word, len(word)) for word in read_words()):
                if length not in words_by_length:
                    words_by_length[length] = set()
                words_by_length[length].add(word)

            anagrams = []
            for length in words_by_length.keys():
                for combo in combinations(words_by_length[length], 2):
                    if sorted(combo[0]) == sorted(combo[1]):
                        anagrams.append(combo)

            return anagrams

        def square_numbers_for_length(length):
            lo = int(math.ceil(math.sqrt(math.pow(10, length-1))))
            hi = int(math.floor(math.sqrt(math.pow(10, length)-1)))
            return [n*n for n in range(lo, 1+hi)]

        def determine_mapping(word, number):
            map = {}
            for (c, n) in zip(word, number):
                if c in map:
                    if map[c] != n:
                        return None
                elif n in map.values():
                    return None
                else:
                    map[c] = n
            return map

        # alrighty, let's use all those helper methods ...

        anagrams = extract_anagrams()

        largest = 0
        square_numbers_by_length = {}
        for (word1, word2) in anagrams:
            length = len(word1)
            if length not in square_numbers_by_length:
                square_numbers_by_length[length] = square_numbers_for_length(length)

            square_numbers = square_numbers_by_length[length]
            for sq in square_numbers:
                map = determine_mapping(word1, str(sq))
                if map is not None:
                    sq2 = int(''.join(map[c] for c in word2))
                    if sq2 in square_numbers:
                        if sq > largest: largest = sq
                        if sq2 > largest: largest = sq2

        return largest

    @staticmethod
    def get_tests():
        return [(None, 18769)]


if __name__ == '__main__':
    print("The answer is", Problem98.solve())
