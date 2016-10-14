"""Problem 15 - Project Euler

   Lattice paths

   Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
   there are exactly 6 routes to the bottom right corner.

   How many such routes are there through a 20×20 grid?
"""

import math


class Problem15(object):
    @staticmethod
    def solve(n=20):
        """This is clearly a combinatorial problem since the results for the first
           few grids look like pascal's triangle:
              2:6, 3:20, 4:70

           Digging around a bit i believe this is calculable as comb(2n,n) which is (2n)! / n!n!
        """
        return int(math.factorial(2*n) / math.factorial(n) / math.factorial(n))

    @staticmethod
    def solve2(n=20):
        """The spirit of this is probably to do a grid and calculate number of paths"""
        n += 1
        grid = [[1] * n] * n
        for row in range(1, n):
            for col in range(1, n):
                grid[row][col] = grid[row][col-1] + grid[row-1][col]
        return grid[-1][-1]


if __name__ == '__main__':
    print("The number of such routes through a 20x20 grid is", Problem15().solve())
