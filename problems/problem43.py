"""Problem 43 - Project Euler

Sub-string divisibility

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits
0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
  | d2d3d4=406 is divisible by 2
  | d3d4d5=063 is divisible by 3
  | d4d5d6=635 is divisible by 5
  | d5d6d7=357 is divisible by 7
  | d6d7d8=572 is divisible by 11
  | d7d8d9=728 is divisible by 13
  | d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""
from itertools import dropwhile


class Problem43(object):
    @staticmethod
    def solve():
        def __all_unique(s):
            return len(s) == len(set(s))

        def __useable_combos(r, f):
            return filter(f, ('0' + str(v) if v < 100 else str(v) for v in dropwhile(lambda x: x < 10, r)))

        def __generate(pq=(17, 13, 11, 7, 5, 3, 2), tail=None, suffix=None):
            """generator for qualified pandigital numbers"""
            if pq:
                p, pq = pq[0], pq[1:]
                # deal with the first iteration requiring different filter and suffix-building
                f = __all_unique if not tail else lambda x: x.endswith(tail) and __all_unique(x[0] + suffix)
                s = (lambda x: x) if not suffix else (lambda x: x[0] + suffix)
                for d in __useable_combos(range(p, 1000, p), f):
                    yield from __generate(pq, d[0:2], s(d))
            else:
                # finished with sub-strings, try to find a valid first digit
                yield from (int(c) for c in filter(__all_unique, (str(d) + suffix for d in range(1, 10))))

        return sum(__generate())


if __name__ == '__main__':
    print("The answer is", Problem43.solve())
