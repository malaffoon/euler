"""Problem 4 - Project Euler

   Largest palindrome product

   A palindromic number reads the same both ways.
   The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

   Find the largest palindrome made from the product of two 3-digit numbers.
"""

import math

class Problem4(object):
    @staticmethod
    def solve():
        """Return the largest palindrome made from the product of two 3-digit numbers"""
        # yeah this isn't elegant or anything; assume it will be from a product of 9xx's
        palindromes = []
        for i in range(900, 1000):
            for j in range(900, 1000):
                value = i*j
                if is_palindrome(value): palindromes.append(value)
        return max(palindromes)


def is_palindrome(value):
    """Return true if string representation of value is a strict palindrome"""
    value = str(value)
    mid = math.floor(len(value) / 2)
    return value[0:mid:1] == value[-1:-mid-1:-1]

if __name__ == '__main__':
    print("The largest palindrome made from the product of two 3-digit numbers is", Problem4().solve())
