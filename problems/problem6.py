"""Problem 6 - Project Euler

Sum square difference

The sum of the squares of the first ten natural numbers is,
    12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
    3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Just gonna use maths here ...
The sum of squares of 1..n = n(n+1)(2n+1)/6
The sum of 1..n = n(n+1)/2, so the square of sum of 1..n = n(n+1)n(n+1)/4
Grind through the algebra and you get the difference = n(n+1)(n-1)(3n+2)/12
"""


class Problem6(object):
    @staticmethod
    def solve(n):
        return n * (n+1) * (n-1) * (3*n+2) // 12


if __name__ == '__main__':
    print("The difference between the sum of the squares of the first one ten natural numbers and the square of the sum is", Problem6().solve(10))
    print("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is", Problem6().solve(100))
