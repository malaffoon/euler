"""Problem 67 - Project Euler

Maximum path sum II

By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

  |    3
  |   7 4
  |  2 4 6
  | 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'),
a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this
problem, as there are 2^99 altogether! If you could check one trillion (10^12) routes every second it would take
over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

Since we don't need the actual path we can just record the maximum total at each cell.
"""

PROBLEM67_EXAMPLE = [
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3]
]


class Problem67(object):
    @staticmethod
    def solve(triangle=None):
        if not triangle:
            with open('../../resources/p067_triangle.txt') as file:
                triangle = [[int(c) for c in line.split(' ')] for line in file.readlines()]

        for r in range(1, len(triangle)):
            for c in range(len(triangle[r])):
                triangle[r][c] = triangle[r][c] + max(triangle[r - 1][max(0, c - 1):min(c, len(triangle[r])) + 1])
        return max(triangle[-1])

    @staticmethod
    def get_tests():
        return [(None, 7273), (PROBLEM67_EXAMPLE, 23)]


if __name__ == '__main__':
    print("The answer is", Problem67.solve())
