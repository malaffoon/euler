"""Problem 85 - Project Euler

Counting rectangles

By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

6 1x1
4 2x1
2 3x1
3 1x2
2 2x2
1 3x2

Although there exists no rectangular grid that contains exactly two million rectangles,
find the area of the grid with the nearest solution.


There is probably some correlation between area and number of rectangles regardless of proportions.
A rectangular grid 6 by 1 has 6 1x1, 5 2x1, 4 3x1, 3 4x1, 2 5x1, 1 6x1 = 21 rectangles
The flat rectangular grid has r(r+1)/2 rectangles, area=r; i'm guessing this is the max for the area???
A square has s*s*s+1 rectangles, area=s*s; i'm guessing this is the min for the area

After much futzing i think the general formula for number of rectangles is m(m+1)n(n+1)/4
Obviously the area is mn
I think a square has the fewest rectangles per area and a square of side 126 has > 2000000 rectangles
so constrain m and n to (1,120) and see how it goes.
"""


class Problem85(object):
    @staticmethod
    def solve():
        closest_count = 0
        closest_area = 0
        for m in range(1, 120):
            for n in range(1, 120):
                count = Problem85._rectangles(m, n)
                if abs(count-2000000) < abs(closest_count-2000000):
                    closest_count = count
                    closest_area = m * n
        return closest_area

    @staticmethod
    def _rectangles(m, n):
        """Return the number of rectangles in a m x n rectangle
        """
        return m * (m+1) * n * (n+1) // 4

    @staticmethod
    def get_tests():
        return [(None, 2772)]


if __name__ == '__main__':
    print("The answer is", Problem85.solve())
