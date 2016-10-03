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

Optimizations:
 * last 3 digits must be divisible by 17
"""
from itertools import dropwhile


class Problem43(object):
    @staticmethod
    def solve():
        # ugly, work-from-end approach:
        def all_unique(s):
            return len(s) == len(set(s))

        def useable_combos(r, f):
            return filter(f, ('0' + str(v) if v < 100 else str(v) for v in dropwhile(lambda x: x < 10, r)))

        def prepend(pq, tail, suffix):
            result = 0
            if pq:
                p, pq = pq[0], pq[1:]
                for d in useable_combos(range(p, 1000, p), lambda x: x.endswith(tail) and all_unique(x[0] + suffix)):
                    result += prepend(pq, d[0:2], d[0] + suffix)
            else:
                for d1 in range(1, 10):
                    candidate = str(d1) + suffix
                    if all_unique(candidate):
                        result += int(candidate)
            return result

        result = 0
        for d17 in useable_combos(range(17, 1000, 17), all_unique):
            result += prepend([13, 11, 7, 5, 3, 2], d17[0:2], d17)
        return result


if __name__ == '__main__':
    print("The answer is", Problem43.solve())
