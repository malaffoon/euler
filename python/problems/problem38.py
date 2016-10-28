"""Problem 38 - Project Euler

Take the number 192 and multiply it by each of 1, 2, and 3:

  | 192 × 1 = 192
  | 192 × 2 = 384
  | 192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated
product of an integer with (1,2, ... , n) where n > 1?
"""

from utils.mathex import is_pandigital


class Problem38(object):
    @staticmethod
    def solve():
        return max(Problem38.__generator__(), key=lambda t: t[0])[0]

    @staticmethod
    def get_tests():
        return [(None, 932718654)]

    @staticmethod
    def __generator__():
        """Generates pandigital concatenated products for this problem

        Returns tuples of (pandigital, number, tuple), e.g. (192384576, 192, (1,2,3))
        """
        # test ranges can be very restrictive since the concatenated product
        # must be 9 digits and must start with 9 (given the examples)
        test_ranges = [((1, 2), range(9123, 9487+1)),
                       # ((1, 2, 3), range(123, 321+1)),
                       # ((1, 2, 3, 4), range(12, 32+1)),
                       ((1, 2, 3, 4, 5), range(9, 9+1))]
        for (tpl, r) in ((tr[0], tr[1]) for tr in test_ranges):
            for n in r:
                s = Problem38.__concatenated_product__(n, tpl)
                if len(s) == 9 and is_pandigital(s):
                    yield (int(s), n, tpl)

    @staticmethod
    def __concatenated_product__(n, tpl):
        """Returns the concatenated product as a string"""
        return ''.join(str(n*p) for p in tpl)


if __name__ == '__main__':
    print("The answer is", Problem38.solve())
