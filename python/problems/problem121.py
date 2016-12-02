"""Problem 121 - Project Euler

Disc game prize fund

A bag contains one red disc and one blue disc. In a game of chance a player takes a disc at random and its
colour is noted. After each turn the disc is returned to the bag, an extra red disc is added, and another
disc is taken at random.

The player pays £1 to play and wins if they have taken more blue discs than red discs at the end of the game.

If the game is played for four turns, the probability of a player winning is exactly 11/120, and so the
maximum prize fund the banker should allocate for winning in this game would be £10 before they would expect
to incur a loss. Note that any payout will be a whole number of pounds and also includes the original £1
paid to play the game, so in the example given the player actually wins £9.

Find the maximum prize fund that should be allocated to a single game in which fifteen turns are played.

probability of winning =
  | probability of 15 blue = probability of 0 red
  | + probability of 14 blue = probability of 1 red
  | ...
  | + probability of 8 blue = probability of 7 red
probability of getting n reds =
  |
"""
import functools as ft
import itertools as it

from utils.mathex import prod


class Problem121(object):
    @staticmethod
    def solve(turns=15):
        den = prod(range(2, 2 + turns))
        num = 1  # number of ways to get 0 red
        for r in range(1, (turns - 1) // 2 + 1):
            num += sum(map(lambda t: prod(t), it.combinations(range(1, turns + 1), r)))

        return den // num

    @staticmethod
    def get_tests():
        return [(None, 2269), (4, 10)]


if __name__ == '__main__':
    print("The answer is", Problem121.solve())
