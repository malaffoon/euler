"""Problem 700 - Project Euler

Eulercoin

Leonhard Euler was born on 15 April 1707.

Consider the sequence 1504170715041707n mod 4503599627370517.

An element of this sequence is defined to be an Eulercoin if it is strictly smaller than all previously found Eulercoins.

For example, the first term is 1504170715041707 which is the first Eulercoin. 
The second term is 3008341430083414 which is greater than 1504170715041707 so is not an Eulercoin. 
However, the third term is 8912517754604 which is small enough to be a new Eulercoin.

The sum of the first 2 Eulercoins is therefore 1513083232796311.

Find the sum of all Eulercoins.

---------------------------------------------------------------------------------------------------
Note that modulo is prime.

Brute force method is (way) too slow, i.e. can't just generate and check every term in the sequence.

I admit to being stumped by this, but i ran across an unrelated blurb that talked about convergence
of mod values; although it sort of makes sense, i don't fully grok it.
"""


class Problem700(object):
    @staticmethod
    def solve():
        n = 1504170715041707
        mod = 4503599627370517
        coins = [n]  # technically, i don't need to collect the coins but there aren't very many
        mn, mx = n, n
        while mn > 1:
            term = (mn + mx) % mod
            if term > mx:
                mx = term
            if term < mn:
                mn = term
                coins.append(term)
        return sum(coins)

    @staticmethod
    def get_tests():
        return [(None, 1517926517777556)]


if __name__ == '__main__':
    print("The answer is", Problem700.solve())
