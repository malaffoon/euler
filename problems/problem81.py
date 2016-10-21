"""Problem 81 - Project Euler

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
by only moving to the right and down, is indicated in bold red and is equal to 2427.

Find the minimal path sum, in matrix.txt, a 31K text file containing a 80 by 80 matrix,
from the top left to the bottom right by only moving right and down.
"""


TEST_DATA = [[131, 673, 234, 103, 18],
             [201, 96, 342, 965, 150],
             [630, 803, 746, 422, 111],
             [537, 699, 497, 121, 956],
             [805, 732, 524, 37, 331]]


class Problem81(object):
    @staticmethod
    def solve(matrix=None):
        if not matrix: matrix = Problem81._read_matrix()
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[row])):
                if col > 0 and row > 0:
                    matrix[row][col] += min(matrix[row][col-1], matrix[row-1][col])
                elif col > 0:
                    matrix[row][col] += matrix[row][col-1]
                elif row > 0:
                    matrix[row][col] += matrix[row-1][col]
        return matrix[-1][-1]

    @staticmethod
    def _read_matrix():
        with open('../resources/p081_matrix.txt') as file:
            return [[int(c) for c in line.split(',')] for line in file.readlines()]


    @staticmethod
    def get_tests():
        return [(None, 427337), (TEST_DATA, 2427)]


if __name__ == '__main__':
    print("The answer is", Problem81().solve())
