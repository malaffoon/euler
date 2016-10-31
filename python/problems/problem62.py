"""Problem 62 - Project Euler

Cubic permutations

The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3).
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""


class Problem62(object):
    @staticmethod
    def solve(p=5):
        # collect cubes of first bunch of numbers, sort each cube and create a multi-map to numbers
        # then just stop when count hits requested value
        cubes = {}
        for n in range(10000):
            c = ''.join(sorted(str(n**3), reverse=True))
            if c in cubes:
                cubes[c].append(n)
                if len(cubes[c]) == p:
                    return cubes[c][0]**3
            else:
                cubes[c] = [n]
        return None

    @staticmethod
    def get_tests():
        return [(None, 127035954683), (3, 41063625)]


if __name__ == '__main__':
    print("The answer is", Problem62.solve())
