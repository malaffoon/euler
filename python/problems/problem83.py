"""Problem 83 - Project Euler

Path sum: four ways

NOTE: This problem is a significantly more challenging version of Problem 81.

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right,
up, and down, is indicated in bold red and is equal to 2297.

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing
a 80 by 80 matrix, from the top left to the bottom right by moving left, right, up, and down.

"""
TEST_DATA = [[131, 673, 234, 103, 18],
             [201, 96, 342, 965, 150],
             [630, 803, 746, 422, 111],
             [537, 699, 497, 121, 956],
             [805, 732, 524, 37, 331]]


class Problem83(object):
    @staticmethod
    def solve(matrix=None):
        if not matrix: matrix = Problem83._read_matrix()

        # handy constants, assumes regular (but not square) matrix
        R = len(matrix)
        C = len(matrix[0])

        # initialize only the top left cell, then iterate, improving min path in each cell

        # create a new matrix that is the minimum sum at each position
        # it starts with None everywhere except the top left corner
        min_matrix = [[None] * C for row in matrix]
        min_matrix[0][0] = matrix[0][0]

        def min_neighbor(r, c):
            def safe_min(*args):
                values = list(filter(lambda x: x is not None, args))
                return None if len(values) == 0 else min(values)

            def safe_min_matrix_ref(r, c):
                return None if (r < 0 or r >= R or c < 0 or c >= C) else min_matrix[r][c]

            return safe_min(safe_min_matrix_ref(r - 1, c), safe_min_matrix_ref(r + 1, c),
                            safe_min_matrix_ref(r, c - 1), safe_min_matrix_ref(r, c + 1))

        changes = True
        while changes:
            changes = False
            for r in range(0, R):
                for c in range(0, C):
                    n = min_neighbor(r, c)
                    if n is not None:
                        if min_matrix[r][c] is None or matrix[r][c] + n < min_matrix[r][c]:
                            changes = True
                            min_matrix[r][c] = matrix[r][c] + n
        return min_matrix[-1][-1]

    @staticmethod
    def _read_matrix():
        with open('../../resources/p083_matrix.txt') as file:
            return [[int(c) for c in line.split(',')] for line in file.readlines()]

    @staticmethod
    def get_tests():
        return [(None, 425185), (TEST_DATA, 2297)]


if __name__ == '__main__':
    print("The answer is", Problem83().solve())
