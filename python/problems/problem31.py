"""Problem 31 - Project Euler

Coin sums

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""


class Problem31(object):
    @staticmethod
    def solve():
        # denominations
        denoms = [1, 2, 5, 10, 20, 50, 100, 200]

        def count_combos_for(amount, max_denom):
            if max_denom == 1: return 1
            # count = 0
            # for denom in (denom for denom in denoms if denom <= max_denom and denom <= amount):
            #     count += 1 if denom == amount else count_combos_for(amount - denom, denom)
            # return count
            return sum(1 if denom == amount else count_combos_for(amount - denom, denom) for denom in denoms if denom <= max_denom and denom <= amount)

        return count_combos_for(200, 200)

    @staticmethod
    def get_tests():
        return [(None, 73682)]


if __name__ == '__main__':
    print("The answer is", Problem31.solve())
