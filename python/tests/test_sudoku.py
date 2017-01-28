import unittest
import time

from utils.sudoku import Sudoku


class SudokuTests(unittest.TestCase):
    def test_solvable(self):
        tests = (
            ('003020600900305001001806400008102900700000008006708200002609500800203009005010300',
             '483921657967345821251876493548132976729564138136798245372689514814253769695417382'),
            ('4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......',
             '417369825632158947958724316825437169791586432346912758289643571573291684164875293'),
            ('85...24..72......9..4.........1.7..23.5...9...4...........8..7..17..........36.4.',
             '859612437723854169164379528986147352375268914241593786432981675617425893598736241'),
            ('..53.....8......2..7..1.5..4....53...1..7...6..32...8..6.5....9..4....3......97..',
             '145327698839654127672918543496185372218473956753296481367542819984761235521839764')
        )
        for (test, expected) in tests:
            start = time.clock()
            sudoku = Sudoku(test)
            sudoku.solve()
            t = time.clock()-start
            self.assertEqual(True, sudoku.solved())
            self.assertEqual(expected, sudoku.ascii_string())
            print("%.2f sec" % (t,))

    def test_unsolvable(self):
        test = '4..7..8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
        sudoku = Sudoku()
        sudoku.parse(test)
        sudoku.solve()
        self.assertEqual(False, sudoku.solved())
        self.assertEqual(test, sudoku.ascii_string())


if __name__ == '__main__':
    unittest.main()


