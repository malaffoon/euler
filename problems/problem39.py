"""Problem 39 - Project Euler

Integer right triangles

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
there are exactly three solutions for p = 120:

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

Optimizations (it took about 30 seconds without any optimizations):
 * p has to be even (try combinations of odd/even a,b and this falls out)
 * given a,p and the two equations a**2+b**2=c**2, a+b+c=p, then you can solve for b
"""

from collections import defaultdict


class Problem39(object):
    @staticmethod
    def solve():
        # convert list of tuples into map of counts
        d = defaultdict(int)
        for (perimeter, sides) in Problem39.__generator__():
            d[perimeter] += 1
        return max(d.items(), key=lambda entry: entry[1])[0]

    @staticmethod
    def __generator__():
        """Generates valid right triangles with perimeters in given range, e.g. (120, (30,40,50))

        Uses optimizations - takes milliseconds
         * p has to be even (try combinations of odd/even a,b and this falls out)
         * you can show c < p/2 so a < p/2
         * given the two equations a**2+b**2=c**2, a+b+c=p, you can solve for b in terms of a,p
        """
        for p in range(12, 1001, 2):
            for a in range(1, p//2):
                b = float(p*(p-2*a)/2/(p-a))
                if b.is_integer():
                    b = int(b)
                    yield (p, (a, b, p - a - b))

    @staticmethod
    def __generator_brute_force__():
        """Generates valid right triangles with perimeters in given range, e.g. (120, (30,40,50))

        Brute force - takes 20-30 seconds, keeping for posterity
        """
        for p in range(12, 1001):
            for a in range(1, p):
                for b in range(a, p):
                    c = p - a - b
                    if c < b: break
                    if a ** 2 + b ** 2 == c ** 2:
                        yield (p, (a, b, c))


if __name__ == '__main__':
    print("The answer is", Problem39.solve())
