"""Problem 60 - Project Euler

Prime pair sets

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in
any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

Algorithm:
 * need a trick for this: brute forcing all the combinations is too slow even with just primes up to 1000 (167)
 * solve1: not elegant but the nested loops thing works in 13 seconds
    * most of the time is spent in the 900,000+ calls to is_prime
 * solve2: get prime pairs that work together, then use that set of pairs to build set of five - 10 seconds
    * most of time spent calculating the pairs (800,000+ calls to is_prime)
 * solve3: generate all primes up to 99,999,999 then just lookup pairings - 39 seconds
    * really really fast once we have primes calculated but that takes too long
"""
from utils.prime import is_prime, primes


class Problem60(object):
    @staticmethod
    def solve():
        return Problem60.solve2()

    @staticmethod
    def solve3():
        lookup = set(primes(100000000))

        def _check(p, *args):
            sp = str(p)
            for o in args:
                so = str(o)
                if not int(sp+so) in lookup or not int(so+sp) in lookup: return False
            return True

        values = list(primes(10000))[1:]  # don't include 2
        for (i1, p1) in enumerate(values):
            for i2 in range(i1 + 1, len(values)):
                p2 = values[i2]
                if not _check(p2, p1): continue
                for i3 in range(i2 + 1, len(values)):
                    p3 = values[i3]
                    if not _check(p3, p1, p2): continue
                    for i4 in range(i3 + 1, len(values)):
                        p4 = values[i4]
                        if not _check(p4, p1, p2, p3): continue
                        for i5 in range(i4 + 1, len(values)):
                            p5 = values[i5]
                            if not _check(p5, p1, p2, p3, p4): continue
                            return sum((p1, p2, p3, p4, p5))


    @staticmethod
    def solve2():
        def _check(p1, p2):
            sp1, sp2 = str(p1), str(p2)
            return is_prime(int(sp1 + sp2)) and is_prime(int(sp2 + sp1))

        # get some primes
        values = list(primes(10000))[1:]  # don't include 2

        # collect possible pairings
        pairings = {}
        for (i1, p1) in enumerate(values):
            pairings[p1] = set(filter(lambda p: _check(p1, p), values[i1 + 1:]))

        # figure out how to combine pairings
        for p1 in values:
            p1p = pairings[p1]
            for p2 in p1p:
                p2p = pairings[p2].intersection(p1p)
                for p3 in p2p:
                    p3p = pairings[p3].intersection(p2p)
                    for p4 in p3p:
                        p4p = pairings[p4].intersection(p3p)
                        for p5 in p4p:
                            return sum((p1, p2, p3, p4, p5))

    @staticmethod
    def solve1():
        def _check(p, *args):
            sp = str(p)
            for o in args:
                so = str(o)
                if not is_prime(int(sp + so)) or not is_prime(int(so + sp)): return False
            return True

        values = list(primes(10000))[1:]  # don't include 2
        for (i1, p1) in enumerate(values):
            for i2 in range(i1 + 1, len(values)):
                p2 = values[i2]
                if not _check(p2, p1): continue
                for i3 in range(i2 + 1, len(values)):
                    p3 = values[i3]
                    if not _check(p3, p1, p2): continue
                    for i4 in range(i3 + 1, len(values)):
                        p4 = values[i4]
                        if not _check(p4, p1, p2, p3): continue
                        for i5 in range(i4 + 1, len(values)):
                            p5 = values[i5]
                            if not _check(p5, p1, p2, p3, p4): continue
                            return sum((p1, p2, p3, p4, p5))

    @staticmethod
    def get_tests():
        return [(None, 26033)]


if __name__ == '__main__':
    print("The answer is", Problem60.solve())
