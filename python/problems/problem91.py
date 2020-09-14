"""Problem 91 - Project Euler

Right triangles with integer coordinates

---------------------------------------------------------------------------------------------------
Seems like there are a couple possible approaches:
1. Count triangles logically, sort of. There are three types:
    a) Those with two integer length sides, i.e. two sides of a rectangle.
    b) Those with integer length hypothenuse and two non-integer sides
    c) Those with three non-integer length sides
2. Brute force it, calculate all triangles, checking slopes.
3. Calculate third points for all second point possibilities. Use known slope to calculate
all integer x2,y2 values. Or something like that.

I played with approach #1, but wasn't sure how to count 1c triangles.

Approach #2 would probably work but seems like a lot of calculations, might be slow.

For approach 3, here are cases (first three involve at least one point on axis):
    a) P1(x1=1..n,y1=0), P2(x2=0,y2=1..n), n*n triangles
    b) P1(x1=1..n,y1=0), P2(x2=x1,y2=1..n), n*n triangles
    c) P1(x1=1..n,y1=y2), P2(x2=0,y2=1..n), n*n triangles
    d) P1(x1=1..n,y1=1..n), P2, where P2 is calculated based on slopes: P2 values will lie on the line
    orthogonal to the line O-P1, i.e. with slope equal to negative inverse of slope of O-P1.
"""
from math import gcd


class Problem91(object):
    @staticmethod
    def solve(n=50):
        total = 3 * n * n  # special cases
        for x1 in range(1, n+1):
            for y1 in range(1, n+1):
                # calculate integer deltas for line orthogonal to O-P1
                f = gcd(x1, y1)
                dx, dy = int(y1/f), int(x1/f)
                total += min((x1-0)//dx, (n-y1)//dy)  # P2 "above" P1
                total += min((n-x1)//dx, (y1-0)//dy)  # P2 "below" P1
        return total

    @staticmethod
    def get_tests():
        return [(2, 14), (50, 14234)]


if __name__ == '__main__':
    print("The answer is", Problem91.solve(50))
