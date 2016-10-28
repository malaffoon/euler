"""Problem 57 - Project Euler

Square root convergents

It is possible to show that the square root of two can be expressed as an infinite continued fraction.
  | √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:
1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the
first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?

Algorithm:
 * starting with 1/1 == 1,1 the next term is (2*d+n)/(d+n) so this should be easy peasy
"""


class Problem57(object):
    @staticmethod
    def solve():
        count = 0
        n, d = 1, 1
        for e in range(1000):
            n, d = 2 * d + n, d + n
            if len(str(n)) > len(str(d)): count += 1
        return count

    @staticmethod
    def get_tests():
        return [(None, 153)]


if __name__ == '__main__':
    print("The answer is", Problem57.solve())
