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

    def test_e(self):
        e = ContinuedFraction.for_e(10)
        self.assertEqual("[2;1,2,1,1,4,1,1,6,1,1,8,1]", str(e))
        self.assertEqual([(2,1),(3,1),(8,3),(11,4),(19,7),(87,32),(106,39),(193,71),(1264,465),(1457,536)], list(e.convergents())[:10])