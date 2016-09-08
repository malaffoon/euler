"""Problem 28 - Project Euler

Number spiral diagonals
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
  | 21 22 23 24 25
  | 20  7  8  9 10
  | 19  6  1  2 11
  | 18  5  4  3 12
  | 17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""


class Problem28(object):
    @staticmethod
    def solve(n=1001):
        # penciling it out, the sum of corners for any "ring" is calculable:
        # r = ring (0 is degenerate center ring)
        # n = 2r+1 (n is the length/width of ring, so 3,5,7,9)
        # sum_ring = 4(n^2-3r) = 4((2r+1)^2-3r) = 4(4r^2+r+1)
        # So, just add 'em all up for r=1,500; don't forget the degenerate 1
        return 1 + sum(4*(4*r*r+r+1) for r in range(1, 1+(n-1)//2))


if __name__ == '__main__':
    print("The answer is", Problem28.solve())
