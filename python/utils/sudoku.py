"""Container for representing and solving Sudoku puzzles

A Sudoku puzzle is a grid of 9x9 squares. Although this code will treat it as a 2D matrix using [r,c] indexing,
here is a snippet of notation (taken from Peter Norvig): the majority of enthusiasts label the columns 1-9,
the rows A-I, and call a collection of nine squares (column, row, or box) a unit and the squares that share a
unit the peers. A puzzle leaves some squares blank and fills others with digits, and the whole idea is:
  | A puzzle is solved if the squares in each unit are filled with a permutation of the digits 1 to 9.
That is, no digit can appear twice in a unit, and every digit must appear once. This implies that each square
must have a different value from any of its peers.

Here are the names of the squares, a typical puzzle, and the solution to the puzzle:
  |  A1 A2 A3| A4 A5 A6| A7 A8 A9    4 . . |. . . |8 . 5     4 1 7 |3 6 9 |8 2 5
  |  B1 B2 B3| B4 B5 B6| B7 B8 B9    . 3 . |. . . |. . .     6 3 2 |1 5 8 |9 4 7
  |  C1 C2 C3| C4 C5 C6| C7 C8 C9    . . . |7 . . |. . .     9 5 8 |7 2 4 |3 1 6
  | ---------+---------+---------    ------+------+------    ------+------+------
  |  D1 D2 D3| D4 D5 D6| D7 D8 D9    . 2 . |. . . |. 6 .     8 2 5 |4 3 7 |1 6 9
  |  E1 E2 E3| E4 E5 E6| E7 E8 E9    . . . |. 8 . |4 . .     7 9 1 |5 8 6 |4 3 2
  |  F1 F2 F3| F4 F5 F6| F7 F8 F9    . . . |. 1 . |. . .     3 4 6 |9 1 2 |7 5 8
  | ---------+---------+---------    ------+------+------    ------+------+------
  |  G1 G2 G3| G4 G5 G6| G7 G8 G9    . . . |6 . 3 |. 7 .     2 8 9 |6 4 3 |5 7 1
  |  H1 H2 H3| H4 H5 H6| H7 H8 H9    5 . . |2 . . |. . .     5 7 3 |2 9 1 |6 8 4
  |  I1 I2 I3| I4 I5 I6| I7 I8 I9    1 . 4 |. . . |. . .     1 6 4 |8 7 5 |2 9 3

Every square is in 3 units (row, column, box), and has 20 peers (8 in row, 8 in column, 4 others in box).
"""
from itertools import product, chain


class Sudoku(object):
    digits = '123456789'
    empty = '0.'

    def __init__(self, grid=None):
        self.values = [['123456789' for c in range(0, 9)] for r in range(0, 9)]
        self.unsolvable = None
        if grid is not None:
            self.parse(grid)

    def __repr__(self):
        return self.ascii_string()

    @staticmethod
    def _ascii(char):
        """Helper to get 'empty' squares as '.'"""
        return char if len(char) == 1 else '.'

    def ascii_string(self):
        """String version of puzzle, e.g.

        4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......
        """
        return ''.join(self._ascii(char) for char in chain.from_iterable(self.values))

    def ascii_grid(self):
        """Return an ascii-art grid string representing the puzzle, e.g.

          | 4 . . |. . . |8 . 5
          | . 3 . |. . . |. . .
          | . . . |7 . . |. . .
          | ------+------+------
          | . 2 . |. . . |. 6 .
          | . . . |. 8 . |4 . .
          | . . . |. 1 . |. . .
          | ------+------+------
          | . . . |6 . 3 |. 7 .
          | 5 . . |2 . . |. . .
          | 1 . 4 |. . . |. . .
        """
        rowline = '\n------+------+------\n'
        return rowline.join(('\n'.join((' |'.join(' '.join(self._ascii(self.values[r][c]) for c in cbox)
                                                  for cbox in ((0, 1, 2), (3, 4, 5), (6, 7, 8)))) for r in rbox)
                             for rbox in ((0, 1, 2), (3, 4, 5), (6, 7, 8))))

    def parse(self, grid):
        """A grid is a sequence of characters with 1-9 indicating a digit, 0 or . specifying an empty square
        and all other characters are ignored. So the following are all valid examples of a puzzle:
          | 4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......
          |
          | 400000805
          | 030000000
          | 000700000
          | 020000060
          | 000080400
          | 000010000
          | 000603070
          | 500200000
          | 104000000
          |
          | 4 . . |. . . |8 . 5
          | . 3 . |. . . |. . .
          | . . . |7 . . |. . .
          | ------+------+------
          | . 2 . |. . . |. 6 .
          | . . . |. 8 . |4 . .
          | . . . |. 1 . |. . .
          | ------+------+------
          | . . . |6 . 3 |. 7 .
          | 5 . . |2 . . |. . .
          | 1 . 4 |. . . |. . .
        """
        chars = [c for c in grid if c in Sudoku.digits or c in Sudoku.empty]
        assert len(chars) == 81
        for (r, c), char in zip(product(range(0, 9), repeat=2), chars):
            self.values[r][c] = '123456789' if char in Sudoku.empty else char
        self.unsolvable = False

    def solve(self):
        # solve against a copy to avoid replacing values if unsolvable
        v = self._search([list(row) for row in self.values])
        if not v:
            self.unsolvable = True
        else:
            self.values = v
            self.unsolvable = False

    def solved(self):
        return self._is_solved(self.values)

    @staticmethod
    def _search(values):
        """Search for a solution by trying values

        Copy values
        Find cell with fewest options, go through them, recursing for each
        """
        values = Sudoku._eliminate(values)
        if not values: return None
        if Sudoku._is_solved(values): return values

        def copy_with_change(values, r, c, d):
            copy = [list(row) for row in values]
            copy[r][c] = d
            return copy

        n, r, c = min((len(values[r][c]), r, c) for r in range(0, 9) for c in range(0, 9) if len(values[r][c]) > 1)
        trials = map(lambda d: Sudoku._search(copy_with_change(values, r, c, d)), values[r][c])
        return next((v for v in trials if v is not None), None)

    @staticmethod
    def _eliminate(values):
        """Return values with simple eliminations performed or False if unsolvable"""
        changes = 1
        while changes:
            changes = 0
            # chain together row, column, and box units
            for unit in chain(
                    ([(r, c) for c in range(0, 9)] for r in range(0, 9)),
                    ([(r, c) for r in range(0, 9)] for c in range(0, 9)),
                    list(map(lambda x: list(product(x[0], x[1])), product(((0, 1, 2), (3, 4, 5), (6, 7, 8)), repeat=2)))
            ):
                # if any squares have a single possible value, eliminate that value from peers
                for tr, tc in ((r, c) for r, c in unit if len(values[r][c]) == 1):
                    d = values[tr][tc]
                    for pr, pc in ((r, c) for r, c in unit if (r, c) != (tr, tc) and d in values[r][c]):
                        values[pr][pc] = values[pr][pc].replace(d, '')
                        changes += 1
                        if len(values[pr][pc]) == 0:
                            return None
                # if a unit has only one possible place for a value, set the value
                for d in '123456789':
                    possible = [(r, c) for r, c in unit if d in values[r][c]]
                    if len(possible) == 0:
                        return None
                    if len(possible) == 1:
                        (r, c) = possible[0]
                        if len(values[r][c]) > 1:
                            values[possible[0][0]][possible[0][1]] = d
                            changes += 1
        return values

    @staticmethod
    def _is_solved(values):
        return all(len(value) == 1 for value in chain.from_iterable(values))


if __name__ == '__main__':
    sudoku = Sudoku()
    sudoku.parse("4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......")
    print(sudoku.ascii_grid())
    print("try solve")
    sudoku.solve()
    print(sudoku.ascii_grid())
