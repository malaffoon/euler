"""Problem 79 - Project Euler

Passcode derivation

A common security method used for online banking is to ask the user for three random characters from a passcode.
For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters;
the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine
the shortest possible secret passcode of unknown length.
"""

import functools as ft
import itertools as it


class Problem79(object):
    @staticmethod
    def solve():
        # this assumes there are no duplicates (i'm sure it could be modified but since there weren't ...)
        # it gets the unique digits, then sorts them using the keylog entries
        def sorter(x, y):
            for key in keys:
                if x in key and y in key:
                    return -1 if key.index(x) < key.index(y) else +1
            return 0

        keys = list(Problem79.read_keylog())
        uniques = list(set(it.chain.from_iterable(keys)))
        return int(''.join(sorted(uniques, key=ft.cmp_to_key(sorter))))

    @staticmethod
    def get_tests():
        return [(None, 73162890)]

    @staticmethod
    def read_keylog():
        with open('../resources/p079_keylog.txt') as file:
            return map(lambda s: s.strip(), file.readlines())


if __name__ == '__main__':
    print("The answer is", Problem79.solve())
