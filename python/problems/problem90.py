"""Problem 90 - Project Euler

Cube digit pairs

Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube.
By placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.

For example, the square number 64 could be formed: (picture of cubes with 6 and 4 showing)

In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below
one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on
the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like
{0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed; otherwise it would
be impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on each cube, not the order.

{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the
extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?

---------------------------------------------------------------------------------------------------
Will/can brute force work?

All possible cube combinations = 10c6 * 10c6 = 44100. Doesn't seem like a lot.
Given a cube combination, how hard is it to calculate that all square numbers can be displayed?
Just see if the digits of the square are in the respective cubes.
Then deal with 6/9 wrinkle: replace 9 with 6 everywhere.

When calculating, either divide by two at the end or count only "upper half" of cube combinations.
"""
from itertools import combinations

squares = ('01', '04', '06', '16', '25', '36', '46', '64', '81')
digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '6')


class Problem90(object):
    @staticmethod
    def solve():
        cubes = [''.join(d) for d in combinations(digits, 6)]
        return sum(1 for i, c1 in enumerate(cubes) for c2 in cubes[:i]
                   if all((sn[0] in c1 and sn[1] in c2) or (sn[0] in c2 and sn[1] in c1) for sn in squares))

    @staticmethod
    def get_tests():
        return [(None, 1217)]


if __name__ == '__main__':
    print("The answer is", Problem90.solve())
