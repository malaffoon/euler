"""Problem 48 - Project Euler

Self powers

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""


class Problem48(object):
    @staticmethod
    def solve(n=1000):
        return str(sum(i**i for i in range(1, n+1)))[-10:]

    @staticmethod
    def get_tests():
        return [(None, '9110846700'), (10, '0405071317')]


if __name__ == '__main__':
    print("The answer is", Problem48.solve())
