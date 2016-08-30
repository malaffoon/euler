""" Problem 18 - Project Euler

Maximum path sum I

By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23:

|    3
|   7 4
|  2 4 6
| 8 5 9 3
|
| That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

|               75
|              95 64
|             17 47 82
|            18 35 87 10
|           20 04 82 47 65
|          19 01 23 75 03 34
|         88 02 77 73 07 63 67
|        99 65 04 28 06 16 70 92
|       41 41 26 56 83 40 80 70 33
|      41 48 72 33 47 32 37 16 94 29
|     53 71 44 65 25 43 91 52 97 51 14
|    70 11 33 28 77 73 17 78 39 68 17 57
|   91 71 52 38 17 14 91 43 58 50 27 29 48
|  63 66 04 68 89 53 67 30 73 16 69 87 40 31
| 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; 
it cannot be solved by brute force, and requires a clever method! ;o)
"""

PROBLEM18_EXAMPLE = [
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3]
]

PROBLEM18_DATA = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]


class Problem18(object):
    @staticmethod
    def solve(triangle=PROBLEM18_DATA):
        # brute force generates all paths and find max
        # i'll wait until problem 67 to figure out the efficient algorithm
        return max(sum(p) for p in path_generator(triangle))


def path_generator(triangle):
    # depth-first
    rows = len(triangle)
    pos = [0] * rows

    def advance_pos():
        for row in range(rows - 1, 0, -1):
            if pos[row] <= len(triangle[row]) and pos[row] == pos[row - 1]:
                pos[row] += 1
                for reset in range(row + 1, rows):
                    pos[reset] = pos[reset - 1]
                return True
        return False

    # pos is the current path position in the triangle, an array of index values into triangle rows
    while True:
        yield (triangle[r][pos[r]] for r in range(rows))
        if not advance_pos():
            break


if __name__ == '__main__':
    print("The maximum total from top to bottom of the triangle is", Problem18().solve())
