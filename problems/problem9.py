"""Problem 9 - Project Euler

   Special Pythagorean triplet

   A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
       a2 + b2 = c2
   For example, 32 + 42 = 9 + 16 = 25 = 52.

   There exists exactly one Pythagorean triplet for which a + b + c = 1000.
   Find the product abc.
"""


class Problem9(object):
    @staticmethod
    def solve():
        """not a whole lot of subtlety in this solution"""
        for a in range(1, 333):
            for b in range(a+1, (1000-a)//2):
                for c in range(b+1, 1000):
                    if a+b+c < 1000: continue
                    if a+b+c > 1000: break
                    if (a*a + b*b) == c*c:
                        print(a, b, c, a*b*c)
                        return a*b*c

if __name__ == '__main__':
    print("The product abc for the triplet is", Problem9().solve())
