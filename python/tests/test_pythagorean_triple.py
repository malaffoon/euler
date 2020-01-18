import unittest

from itertools import takewhile
from utils.pythagorean_triple import generator


class PythagoreanTripleTests(unittest.TestCase):
    def test_if_no_limit_and_not_primitive(self):
        with self.assertRaises(ValueError):
            _sort_triple_list(generator(limit=None, primitive=False))

    def test_without_limit(self):
        self.assertEqual([(3, 4, 5), (5, 12, 13), (7, 24, 25), (8, 15, 17), (9, 40, 41), (11, 60, 61), (12, 35, 37),
                          (13, 84, 85), (16, 63, 65), (20, 21, 29), (28, 45, 53), (33, 56, 65), (48, 55, 73)],
                         _sort_triple_list(takewhile(lambda x : sum(x) < 200, generator())))

    def test_with_limit(self):
        self.assertEqual([(3, 4, 5)],
                         _sort_triple_list(generator(12, primitive=False)))
        self.assertEqual([(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (9, 40, 41),
                          (10, 24, 26), (12, 16, 20), (12, 35, 37), (15, 20, 25), (18, 24, 30), (20, 21, 29),
                          (21, 28, 35), (24, 32, 40)],
                         _sort_triple_list(generator(108, primitive=False)))

    def test_primitive_with_limit(self):
        self.assertEqual([(3, 4, 5)],
                         _sort_triple_list(generator(12)))
        self.assertEqual([(3, 4, 5), (5, 12, 13), (7, 24, 25), (8, 15, 17), (9, 40, 41), (12, 35, 37), (20, 21, 29)],
                         _sort_triple_list(generator(108)))
        pass


# necessary evil because it make asserting easier
def _sort_triple_list(triples):
    return sorted(tuple(sorted(t)) for t in triples)


if __name__ == '__main__':
    unittest.main()