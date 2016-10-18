"""Problem 50 - Project Euler

Consecutive prime sum

The prime 41, can be written as the sum of six consecutive primes:
 41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
from utils.prime import primes, is_prime


class Problem50(object):
    @staticmethod
    def solve(n=1000000):
        longest = (5, 2)
        p = tuple(primes(n//2))
        for start in range(0, len(p)):
            for stop in range(start+longest[1]+1, len(p)+1):
                s = sum(p[start:stop])
                if s > n:
                    break
                if not is_prime(s):
                    continue
                longest = (s, stop-start)
        return longest[0]

    @staticmethod
    def get_tests():
        return [(None, 997651), (100, 41), (1000, 953)]


if __name__ == '__main__':
    print("The answer is", Problem50.solve())
