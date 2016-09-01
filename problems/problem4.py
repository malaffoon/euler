"""Problem 4 - Project Euler

   Largest palindrome product

   A palindromic number reads the same both ways.
   The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

   Find the largest palindrome made from the product of two 3-digit numbers.
"""

class Problem4(object):
    @staticmethod
    def solve():
        """Return the largest palindrome made from the product of two 3-digit numbers"""
        def is_palindrome(value):
            s = str(value)
            return s == s[::-1]

        # yeah this isn't elegant or anything; assume it will be from a product of 9xx's
        return max(prod for prod in (i*j for i in range(900, 1000) for j in range(i, 1000)) if is_palindrome(prod))


if __name__ == '__main__':
    print("The largest palindrome made from the product of two 3-digit numbers is", Problem4().solve())
