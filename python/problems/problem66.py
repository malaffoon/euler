"""Problem 66 - Project Euler

Diophantine equation

Consider quadratic Diophantine equations of the form:
  | x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 – 2×2^2 = 1
2^2 – 3×1^2 = 1
9^2 – 5×4^2 = 1
5^2 – 6×2^2 = 1
8^2 – 7×3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

After struggling with some brute force methods, i looked up Pell's equation
and found a cool thing about "Fundamental solution via continued fractions".
https://en.wikipedia.org/wiki/Pell%27s_equation
"""
from utils.continued_fraction import ContinuedFraction


class Problem66(object):
    @staticmethod
    def solve(maxD=1000):

        def minimalSolutionInX(D):
            for x, y in ContinuedFraction.forSqrtOf(D).convergents():
                if x*x - D*y*y == 1:
                    return x, y, D
            return None

        return max(map(minimalSolutionInX, range(2, maxD+1)), key=lambda r: r[0] if r else 0)[2]
        # return max((soln for soln in map(minimalSolutionInX, range(2, maxD+1)) if soln), key=lambda r: r[0])[2]

    @staticmethod
    def get_tests():
        return [(None, 661), (7, 5)]


if __name__ == '__main__':
    print("The answer is", Problem66.solve())
