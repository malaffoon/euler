"""Problem 54 - Project Euler

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

  | High Card: Highest value card.
  | One Pair: Two cards of the same value.
  | Two Pairs: Two different pairs.
  | Three of a Kind: Three cards of the same value.
  | Straight: All cards are consecutive values.
  | Flush: All cards of the same suit.
  | Full House: Three of a kind and a pair.
  | Four of a Kind: Four cards of the same value.
  | Straight Flush: All cards are consecutive values of same suit.
  | Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins;
for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie,
for example, both players have a pair of queens, then highest cards in each hand are compared
(see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the first five are
Player 1's cards and the last five are Player 2's cards. You can assume that all hands are
valid (no invalid characters or repeated cards), each player's hand is in no specific order,
and in each hand there is a clear winner.

How many hands does Player 1 win?

5H 5C 6S 7S KD -> Pair of Fives
2C 3S 8S 8D TD -> Pair of Eights

5D 8C 9S JS AC 2C 5C 7D 8S QH
Highest card Ace vs. Highest card Queen

2D 9C AS AH AC 3D 6D 7D TD QD
Three Aces vs. Flush with Diamonds

4D 6S 9H QH QC 3D 6D 7H QD QS
Pair of Queens vs. Highest card Nine
"""


class Problem54(object):
    @staticmethod
    def solve():
        return sum(1 for c in (Problem54._cmp_hands(h1, h2) for h1, h2 in Problem54._read_hands()) if c == +1)

    @staticmethod
    def get_tests():
        return [(None, 376)]

    @staticmethod
    def _read_hands():
        with open('../../resources/p054_poker.txt') as file:
            return map(lambda cards: (cards[0:5], cards[5:10]), map(lambda line: line.strip().split(' '), file.readlines()))

    @staticmethod
    def _cmp_hands(h1, h2):
        for z in zip(Problem54._eval_hand(h1), Problem54._eval_hand(h2)):
            if z[0] < z[1]:
                return -1
            elif z[0] > z[1]:
                return +1
        return 0

    @staticmethod
    def _eval_hand(hand):
        """Evaluate a poker hand, returning a comparable tuple

        hand is expected to be tuple of five pairs of characters: rank+suit, e.g. 5D,8C,9S,JS,AC

        Return is a tuple of comparable values
          | straight flush: 9, high-rank
          | four of a kind: 8, tuple-rank, kicker
          | full house:     7, triple-rank, pair-rank
          | flush:          6, high-rank, next-rank, ...
          | straight:       5, high-rank
          | three of a kind: 4, triple-rank, high-rank, next-rank
          | two pair:       3, high-pair-rank, next-pair-rank, kicker
          | pair:           2, high-rank, next-rank, ...
          | high card:      1, high-rank, next-rank, ...
        """

        def straight(ranks):
            # straight is 0 (no straight), 1 (low straight), or 2 (high straight)
            if len(set(ranks)) < 5:
                return 0
            if max(ranks) - min(ranks) == 4:
                return 2
            if ranks == [12, 3, 2, 1, 0]:  # ace-low straight
                return 1

        ranks = sorted(map(lambda h: '23456789TJQKA'.index(h[0]), hand), reverse=True)
        uniqueranks = set(ranks)

        if len(set(c[1] for c in hand)) == 1:
            # flush or straight flush
            straight = straight(ranks)
            if straight == 2: return 9, ranks[0]
            if straight == 1: return 9, 3
            return 6, ranks[0], ranks[1], ranks[2], ranks[3], ranks[4]
        elif len(uniqueranks) == 2:
            # four of a kind or full house
            c = ranks.count(ranks[0])
            if c == 1: return 8, ranks[1], ranks[0]
            if c == 4: return 8, ranks[0], ranks[4]
            if c == 2: return 7, ranks[2], ranks[0]
            if c == 3: return 7, ranks[0], ranks[3]
        elif len(uniqueranks) == 3:
            # three of a kind or two pair
            c = ranks.count(ranks[0])
            if c == 3: return 4, ranks[0], ranks[3], ranks[4]
            if c == 2:
                if ranks.count(ranks[2]) == 2: return 3, ranks[0], ranks[2], ranks[4]
                else: return 3, ranks[0], ranks[3], ranks[2]
            c = ranks.count(ranks[1])
            if c == 3: return 4, ranks[1], ranks[0], ranks[4]
            if c == 2: return 3, ranks[1], ranks[3], ranks[0]
            return 4, ranks[2], ranks[0], ranks[1]
        elif len(uniqueranks) == 4:
            # pair
            if ranks.count(ranks[0]) == 2: return 2, ranks[0], ranks[2], ranks[3], ranks[4]
            if ranks.count(ranks[1]) == 2: return 2, ranks[1], ranks[0], ranks[3], ranks[4]
            if ranks.count(ranks[2]) == 2: return 2, ranks[2], ranks[0], ranks[1], ranks[4]
            return 2, ranks[3], ranks[0], ranks[1], ranks[2]
        else:
            # straight or high card
            straight = straight(ranks)
            if straight == 2: return 5, ranks[0]
            if straight == 1: return 5, 3
            return 1, ranks[0], ranks[1], ranks[2], ranks[3], ranks[4]


if __name__ == '__main__':
    print("The answer is", Problem54.solve())
