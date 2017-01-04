"""Problem 82 - Project Euler

Path sum: three ways

NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell
in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing
a 80 by 80 matrix, from the left column to the right column.
"""


TEST_DATA = [[131, 673, 234, 103, 18],
             [201, 96, 342, 965, 150],
             [630, 803, 746, 422, 111],
             [537, 699, 497, 121, 956],
             [805, 732, 524, 37, 331]]


class Problem82(object):
    @staticmethod
    def solve(matrix=None):
        if not matrix: matrix = Problem82._read_matrix()

        # handy constants, assumes regular matrix
        R = len(matrix)
        C = len(matrix[0])

        # this approach calculates the minimum sum for every cell in the matrix

        # create a new matrix that is the minimum sum at each position
        # it starts with column 0 values, everything else is None indicating unknown
        min_matrix = [[row[0]] + [None] * (C-1) for row in matrix]

        for c in range(1, C):
            changes = True
            while changes:
                changes = False
                for r in range(0, R):
                    if min_matrix[r][c] is None:
                        min_matrix[r][c] = min_matrix[r][c-1] + matrix[r][c]
                        changes = True
                        continue
                    if r > 0 and min_matrix[r-1][c] is not None and min_matrix[r][c] > (min_matrix[r-1][c] + matrix[r][c]):
                        min_matrix[r][c] = min_matrix[r-1][c] + matrix[r][c]
                        changes = True
                    if r < R-1 and min_matrix[r+1][c] is not None and min_matrix[r][c] > (min_matrix[r+1][c] + matrix[r][c]):
                        min_matrix[r][c] = min_matrix[r+1][c] + matrix[r][c]
                        changes = True
        return min(row[-1] for row in min_matrix)

    @staticmethod
    def _read_matrix():
        with open('../../resources/p082_matrix.txt') as file:
            return [[int(c) for c in line.split(',')] for line in file.readlines()]


    @staticmethod
    def get_tests():
        return [(None, 260324), (TEST_DATA, 994)]


if __name__ == '__main__':
    print("The answer is", Problem82().solve())
