"""Problem 102 - Project Euler

Triangle containment

Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000,
such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates
of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above.
"""


class Problem102(object):
    @staticmethod
    def solve():
        origin = (0, 0)
        count = 0
        # read lines, trimming and splitting on comma
        with open('../../resources/p102_triangles.txt', 'r') as file:
            # TODO - make this more pythonic, use zip?
            for values in map(lambda line: line.strip().split(','), file.readlines()):
                a, b, c = (int(values[0]), int(values[1])), (int(values[2]), int(values[3])), (int(values[4]), int(values[5]))
                if Problem102._point_in_triangle(origin, a, b, c):
                    count += 1
        return count

    @staticmethod
    def _point_in_triangle(p, a, b, c):
        """Determine if the given point, p, is in the triangle defined by a,b,c
        Stole this from the internet somewhere

        :param p: point (x,y)
        :param a: triangle vertex (x,y)
        :param b: triangle vertex (x,y)
        :param c: triangle vertex (x,y)
        :return: True if point in triangle, False otherwise
        """
        def _subtract(m, n):
            return (m[0] - n[0], m[1] - n[1])

        def _check(v, w):
            return v[0]*w[1] - v[1]*w[0] > 0

        vp = _subtract(p, a)
        pb = _check(_subtract(b,a), vp)
        if _check(_subtract(c, a), vp) == pb: return False
        if _check(_subtract(c, b), _subtract(p, b)) != pb: return False
        return True

    @staticmethod
    def get_tests():
        return [(None, 228)]


if __name__ == '__main__':
    print("The answer is", Problem102.solve())
