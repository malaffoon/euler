"""Problem 94 - Project Euler

Almost equilateral triangles

It is easily proved that no equilateral triangle exists with integral length sides and integral area.
However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the
third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area
and whose perimeters do not exceed one billion (1,000,000,000).

---------------------------------------------------------------------------------------------------
Isosceles triangle has two sides of length a, and a base side, b.
Area of such a triangle is b/2 * sqrt(a^2 - b^2/4).

For an almost equilateral triangle b = a +- 1.
For area to be integral, then a^2 - b^2/4 has to be a perfect square.
So, of course, it has to be an integer; which means b has to be even; thus a must be odd.
Of course, b times the square root has to be even (so either b is even or it is a perfect square of an even number).
The perimeter is 2a+b ~ 3a as we get up there, so a:2..1e9/3.

There is probably some magic math around that perfect square thingy.

I doubt brute force will work because of so many values for a. I tried it (see below) but not only did
it take well over one minute, it missed one of the triangles.

Cheated a bit and learned that one way to solve this is to coerce the algebra so you end up with
a Pell's equation in a,h. Reminder Pell's equation have the form x^2 - ny^2 = 1, n is a nonsquare integer.
The solutions to a Pell's equation can be calculated easily as a series, and grow very quickly.
So let's play with the equations ...

h^2 = a^2 - b^2/4
... replace b = a + 1
h^2 = (3a^2 - 2a - 1) / 4
... rearrange it into something Pell-adjacent
3a^2 - 2a - 4h^2 = 1
... complete the square, 3a^2 - 2a = 3(a - 1/3)^2 - 1/3
3(a - 1/3)^2 - 4h^2 = 4/3
... multiply both sides by 3/4 and force a term into single squared thingy:
((3a-1)/2)^2 - 3h^2 = 1
Yay, Pell's with x = (3a-1)/2, y = h, n = 3

Similarly solve for b = a - 1 gives Pells' with x = (3a+1)/2, y = h, n = 3

Look up (https://en.wikipedia.org/wiki/Pell's_equation) Pell's for n=3 (x1,y1) = (2,1)
and generate the sequence, calculating h = y, a = (2x +- 1)/3.
"""
from utils.mathex import pell_gen


class Problem94(object):
    @staticmethod
    def solve():
        sum = 0
        for (x, y) in pell_gen(3):
            if (x, y) == (2, 1): continue   # skip first term, gives non-sensical result
            if x > 500000000: break     # perimeter exceeds limit

            a = (2 * x + 1) / 3  # b = a + 1
            if a.is_integer():
                a, b = int(a), int(a) + 1
                if (b * y / 2).is_integer():
                    sum += a + a + b
            a = (2 * x - 1) / 3  # b = a - 1
            if a.is_integer():
                a, b = int(a), int(a) - 1
                if (b * y / 2).is_integer():
                    sum += a + a + b
        return sum

    @staticmethod
    def get_tests():
        return [(None, 518408346)]


if __name__ == '__main__':
    print("The answer is", Problem94.solve())


"""
Brute force run took about 5 minutes:
5,5,6
17,17,16
65,65,66
241,241,240
901,901,902
3361,3361,3360
12545,12545,12546
46817,46817,46816
174725,174725,174726
652081,652081,652080
2433601,2433601,2433602
9082321,9082321,9082320
33895685,33895685,33895686
The answer is 138907096

But that answer is not correct; clearly missing something. Apparently there is one more 
"""