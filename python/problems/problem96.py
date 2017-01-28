""" Problem 96 - Project Euler

Su Doku

Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear,
but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea
called Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a
9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an
example of a typical starting puzzle grid and its solution grid.

A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary
to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this).
The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because
it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles
ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid;
for example, 483 is the 3-digit number found in the top left corner of the solution grid above.
"""
from utils.sudoku import Sudoku


class Problem96(object):
    @staticmethod
    def solve():
        sum = 0
        for puzzle in Problem96.read_sudoku():
            sudoku = Sudoku(puzzle)
            sudoku.solve()
            sum += int(sudoku.ascii_string()[0:3])
        return sum

    @staticmethod
    def get_tests():
        return [(None, 24702)]

    @staticmethod
    def read_sudoku():
        """read input file yielding sudoku puzzle input; each entry is like

        | Grid 01
        | 003020600
        | 900305001
        | 001806400
        | 008102900
        | 700000008
        | 006708200
        | 002609500
        | 800203009
        | 005010300
        """
        with open('../../resources/p096_sudoku.txt') as file:
            return [s[2:] for s in ''.join(map(lambda s: s.strip(), file.readlines())).split('Grid ')][1:]


if __name__ == '__main__':
    print("The answer is", Problem96().solve())
