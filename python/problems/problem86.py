"""Problem 86 - Project Euler

Cuboid route

A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner.
By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is
shown on the diagram.


However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't
always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions, up to a
maximum size of M by M by M, for which the shortest route has integer length when M = 100. This is the least value
of M for which the number of solutions first exceeds two thousand; the number of solutions when M = 99 is 1975.

Find the least value of M such that the number of solutions first exceeds one million.

---------------------------------------------------------------------------------------------------
For a cube with sides a, b, c, sorted by magnitude, the shortest path L can be calculated by
L^2 = a^2 + (b + c)^2. L will be an integer if that is a perfect square.

Brute force gives me these values:
M=10   ->      14
M=100  ->    2060
M=1000 ->  281334
M=1800 ->  986995
M=1900 -> 1105392
M=2000 -> 1229543


Is there a way to flip this? To be a solution a perfect square has to be the sum of two other
perfect squares. For example 100 = 36 + 64. Then the sum provides N solutions where the sqrt
of one is a side, and the sqrt of the other is the sum of the other two side. For this example,
100 = 36 + 64 -> 6,8 -> {6,1,7},{6,2,6},{6,3,5},{6,4,4},{8,1,5},{8,2,4},{8,3,3}.

Which reeks of Pythagorean triples. The sequence of (non-primitive) Pythagorean triples will
produce the allowed values. For example (3, 4, 5) corresponds 25 = 9 + 16. From that, the sides
for L=5 are {3,1,3},{3,2,2},{1,2,4}. Obviously, multiplying that triple by 2 gives the previous
example of 100 = 36 + 64.

Last step is generating all possible combinations given two numbers. Using the first example,
expand (6,8) into the set of tuples shown above.


Probably there is a better approach that doesn't have to "restart" for each m. Clearly, all the
solutions from the previous m will count and not have to be revisited. Perhaps we could just
keep generating Pythagorean triples, somehow partitioning the counts by largest m used. Meh.
"""


class Problem86(object):
    @staticmethod
    def solve():
        # binary search using best solver
        lower, upper = 0, 2000
        while upper - lower > 1:
            current = (lower+upper) // 2
            solutions = Problem86._pythagorean_solutions_for_m(current)
            if solutions < 1000000:
                lower = current
            else:
                upper = current
        return upper


    @staticmethod
    def _pythagorean_solutions_for_m(m: int) -> int:
        from utils.pythagorean_triple import generator

        cuboids = set()
        # TODO - not sure what to use as limit, since pythagorean generator is ... not exactly predictable
        for t in (tuple(sorted(triple)) for triple in generator(limit=6*m, primitive=False)):
            if t[0] <= m:
                for (a, b) in ((a, t[1] - a) for a in range(1, 1 + t[1] // 2) if a <= t[0] and (t[1] - a) <= t[0]):
                    cuboids.add(tuple(sorted((t[0], a, b))))
            if t[1] <= m:
                for (a, b) in ((a, t[0] - a) for a in range(1, 1 + t[0] // 2) if a <= t[1] and (t[0] - a) <= t[1]):
                    cuboids.add(tuple(sorted((a, b, t[1]))))
        return len(cuboids)

    @staticmethod
    def _brute_force_solutions_for_m(m: int) -> int:
        perfect_squares = set([n*n for n in range(1, 5*m +1)])
        cuboids = set()
        for a in range(1, m+1):
            for b in range(1, a+1):
                for c in range(b, a+1):
                    L2 = a*a + (b+c)*(b+c)
                    if L2 in perfect_squares:
                        sides = (a, c, b)
                        if sides not in cuboids:
                            cuboids.add(sides)
        return len(cuboids)

    @staticmethod
    def get_tests():
        return [(None, 1818)]


if __name__ == '__main__':
    print("The answer is", Problem86.solve())
