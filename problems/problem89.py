"""Problem 89 - Project Euler

Roman numerals

For a number written in Roman numerals to be considered valid there are basic rules which must be followed.
Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way
of writing a particular number.

For example, it would appear that there are at least six ways of writing the number sixteen:
  | IIIIIIIIIIIIIIII
  | VIIIIIIIIIII
  | VVIIIIII
  | XIIIIII
  | VVVI
  | XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be
the most efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers
written in valid, but not necessarily minimal, Roman numerals;
see About... Roman Numerals for the definitive rules for this problem.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.

Denominations:
  | I = 1
  | V = 5
  | X = 10
  | L = 50
  | C = 100
  | D = 500
  | M = 1000

Rules:
  | Numerals must be arranged in descending order of size.
  | M, C, and X cannot be equalled or exceeded by smaller denominations.
  | D, L, and V can each only appear once.
Rules for subtractive combinations:
  | Only one I, X, and C can be used as the leading numeral in part of a subtractive pair.
  | I can only be placed before V and X.
  | X can only be placed before L and C.
  | C can only be placed before D and M.

Common Reductions (given all the caveats)
  | VIIII -> IX
  | IIII -> IV  (but not if it duplicates V)
  | LXXXX -> XC
  | XXXX -> XL  (but not if it duplicates L)
  | DCCCC -> CM
  | CCCC -> CD  (but not if it duplicates D)
"""


class Problem89(object):
    @staticmethod
    def solve():
        def minimal(r):
            return r\
                .replace('VIIII', 'IX').replace('IIII', 'IV')\
                .replace('LXXXX', 'XC').replace('XXXX', 'XL')\
                .replace('DCCCC', 'CM').replace('CCCC', 'CD')
        return sum(len(r) - len(minimal(r)) for r in Problem89.read_romans())

    @staticmethod
    def read_romans():
        with open('../resources/p089_roman.txt') as file:
            return map(lambda s: s.strip(), file.readlines())


if __name__ == '__main__':
    print("The answer is", Problem89.solve())
