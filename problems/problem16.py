"""Problem 16 - Project Euler

   Power digit sum

   2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

   What is the sum of the digits of the number 2^1000?
"""


class Problem16(object):
    @staticmethod
    def solve(n=1000):
        # Python makes this easy ...
        return sum(int(c) for c in str(2**n))


if __name__ == '__main__':
    print("The sum of the digits of the number 2^1000 is", Problem16().solve())
