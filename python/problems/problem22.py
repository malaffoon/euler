""" Problem 22 - Project Euler

Using p022_names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

NOTE: file contains double-quoted names separated by commas, e.g.
    "ALICE","BOB","CHARLIE", ...
"""


class Problem22(object):
    @staticmethod
    def solve(filename='../../resources/p022_names.txt'):
        return sum(score(pos, name) for (pos, name) in enumerate(sorted(read_names(filename)), start=1))

    @staticmethod
    def get_tests():
        return [(None, 871198282)]


def read_names(filename):
    with open(filename, 'r') as file:
        return (s.strip('"') for s in file.read().split(','))


def score(pos, name):
    return pos * sum(ord(c) - ord('A') + 1 for c in name)


if __name__ == '__main__':
    print("The total of all the name scores in the file is", Problem22().solve())