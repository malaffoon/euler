"""Problem 76 - Project Euler

Counting summations

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

Algorithm
 * doh, see problem 31; instead of limited coin denominations we have the values [1..99]

  | f(1) = 0
  | f(2) = 1
  | f(3) = 2
  | f(4) = 4
  | f(5) = 6
  | f(6) = 10
  | f(7) = 14
  | f(8) = 21
  | f(9) = 29
"""


class Problem76(object):
    @staticmethod
    def solve(N=100):
        # non-recursive approach
        combos = [1] + [0] * N
        for n in range(1, N):
            for i in range(n, N+1):
                combos[i] += combos[i-n]
        return combos[N]

    @staticmethod
    def get_tests():
        return [(None, 190569291), (5, 6)]


if __name__ == '__main__':
    print("The answer is", Problem76.solve())
