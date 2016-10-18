"""Problem 36 - Project Euler

Double-base palindromes

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

Note: there are a couple ways to convert a number to binary:
  | >>> bin(585)
  | '0b1001001001'
  |
  | >>> "{0:b}".format(585)
  | '1001001001'

Performance-wise, they are all fast but bin(x) is fastest:
  | >>> timeit.timeit('bin(585)[2:]', setup='', number=1000000) / 1000000
  | 0.00000022
  | >>> timeit.timeit('"{0:b}".format(585)', setup='', number=1000000) / 1000000
  | 0.00000036
"""


class Problem36(object):
    @staticmethod
    def solve(limit=1000000):

        def is_palindrome(s):
            return s == s[::-1]

        return sum(n for n in range(1, limit, 2) if is_palindrome(str(n)) and is_palindrome(bin(n)[2:]))

    @staticmethod
    def get_tests():
        return [(1000000, 872187), (10, 25)]


if __name__ == '__main__':
    print("The answer is", Problem36.solve())
