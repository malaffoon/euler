"""Problem 56 - Project Euler

Powerful digit sum

A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
"""


class Problem56(object):
    @staticmethod
    def solve():
        return max(sum(int(d) for d in str(a**b)) for a in range(100) for b in range(100))

    @staticmethod
    def get_tests():
        return [(None, 972)]


if __name__ == '__main__':
    print("The answer is", Problem56.solve())
