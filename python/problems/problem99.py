"""Problem 99 - Project Euler

Largest exponential

Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would
confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain
over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines
with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.

Algorithm
Uhmmm, can't we just do logarithmic math?
"""
from math import log


class Problem99(object):
    @staticmethod
    def solve():
        # read lines, trimming and splitting on comma
        # for each line, calculate exp*log(base)
        # enumerate to get line numbers
        # get maximum value (return the line number not the value)
        with open('../../resources/p099_base_exp.txt', 'r') as file:
            return max(enumerate(map(lambda entry: float(entry[1]) * log(float(entry[0])),
                        map(lambda line: line.strip().split(','), file.readlines())), 1), key=lambda enum: enum[1])[0]

    @staticmethod
    def get_tests():
        return [(None, 0)]


if __name__ == '__main__':
    print("The answer is", Problem99.solve())
