"""Problem 25 - Project Euler

   1000-digit Fibonacci number

   The Fibonacci sequence is defined by the recurrence relation:
      Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
   Hence the first 12 terms will be:
   The 12th term, 144, is the first term to contain three digits.

   What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

import math


class Problem25(object):
    @staticmethod
    def solve(digits=1000):
        """I just did the algebra on this one ...

           F(n) ~ Phi^n / sqrt(5)
           We want F(n) >= 10^999.
           Solve for n.
              n >= (999 + log10(sqrt(5)) / log10(Phi)
        """
        sqrt5 = math.sqrt(5)
        Phi = (1 + sqrt5)/2

        return math.ceil((digits - 1 + math.log10(sqrt5)) / math.log10(Phi))

    @staticmethod
    def get_tests():
        return [(1000, 4782), (3, 12)]

if __name__ == '__main__':
    print("The index of the first term in the Fibonacci sequence to contain 1000 digits is", Problem25().solve())
