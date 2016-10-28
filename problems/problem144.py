"""Problem 144 - Project Euler

Investigating multiple reflections of a laser beam

In laser physics, a "white cell" is a mirror system that acts as a delay line for the laser beam.
The beam enters the cell, bounces around on the mirrors, and eventually works its way back out.

The specific white cell we will be considering is an ellipse with the equation 4x^2 + y^2 = 100

The section corresponding to −0.01 ≤ x ≤ +0.01 at the top is missing, allowing the light to enter
and exit through the hole.

The light beam in this problem starts at the point (0.0,10.1) just outside the white cell,
and the beam first impacts the mirror at (1.4,-9.6).

Each time the laser beam hits the surface of the ellipse, it follows the usual law of reflection
"angle of incidence equals angle of reflection." That is, both the incident and reflected beams make
the same angle with the normal line at the point of incidence.

In the figure on the left, the red line shows the first two points of contact between the laser beam
 and the wall of the white cell; the blue line shows the line tangent to the ellipse at the point of
 incidence of the first bounce.

The slope m of the tangent line at any point (x,y) of the given ellipse is: m = −4x/y

The normal line is perpendicular to this tangent line at the point of incidence.

The animation on the right shows the first 10 reflections of the beam.

How many times does the beam hit the internal surface of the white cell before exiting?
"""
import math


class Problem144(object):
    @staticmethod
    def solve():
        def reflection(line, point):
            # inputs are incident and base line slopes
            base_slope = -4 * point[0] / point[1]
            t2 = (2 * base_slope) / (1 - base_slope * base_slope)
            m = (t2 - line[0]) / (1 + line[0] * t2)
            b = point[1] - m * point[0]
            return m, b

        def intersections(line):
            # line input is (m,b) tuple
            a = line[0] * line[0] + 4
            b = 2 * line[0] * line[1]
            c = line[1] * line[1] - 100
            x1 = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
            x2 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)
            return (x1, line[0]*x1 + line[1]), (x2, line[0]*x2 + line[1])

        line = (-9.6 - 10) / 1.4, 10
        point = (1.4, -9.6)
        for i in range(10):
            print(line, intersections(line))
            line = reflection(line, point)
            points = intersections(line)
            # TODO - need to round and do approximate equals to pick other point
            # TODO   and/or change algorithm to automatically get other point
            point = points[0] if point[1] != points[0][1] else points[1]
            print("   point", point)

        return 0

    @staticmethod
    def get_tests():
        return []


if __name__ == '__main__':
    print("The answer is", Problem144.solve())
