import unittest

import itertools

from utils.continued_fraction import ContinuedFraction


class ContinuedFractionTests(unittest.TestCase):
    def test_forSqrtOf(self):
        self.assertEqual("[2;(1,1,1,4)]", str(ContinuedFraction.forSqrtOf(7)))
        self.assertEqual("[2;]", str(ContinuedFraction.forSqrtOf(4)))

    def test_forRational(self):
        self.assertEqual("[3;4,12,3,1]", str(ContinuedFraction.forRational(3.245)))
        self.assertEqual("[2;3,7]", str(ContinuedFraction.forRational(1071/462)))
        self.assertEqual("[2;]", str(ContinuedFraction.forRational(2)))

    def test_convergents(self):
        self.assertEqual([(0,1),(1,1),(5,6),(11,13),(27,32)], list(ContinuedFraction(0, (1,5,2,2)).convergents()))
        self.assertEqual([(1,1),(2,1),(5,3),(7,4),(19,11),(26,15),(71,41),(97,56)], list(itertools.islice(ContinuedFraction.forSqrtOf(3).convergents(), 0, 8)))

