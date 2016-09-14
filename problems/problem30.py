"""Problem 30 - Project Euler

Digit fifth powers

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

NOTE: algorithmically very similar to Problem 34
"""


class Problem30(object):
    @staticmethod
    def solve(p=5):
        def is_sum(n):
            return n == sum(int(d)**p for d in str(n))

        # max number to consider is approximately (p+1)*9^p
        return sum(n for n in range(10, int((p+1)*(9**p))) if is_sum(n))


if __name__ == '__main__':
    print("The sum of all the numbers that can be written as the sum of fifth powers of their digits is", Problem30.solve())
