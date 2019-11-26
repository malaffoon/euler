""" Problem 387 - Project Euler

A Harshad or Niven number is a number that is divisible by the sum of its digits.
201 is a Harshad number because it is divisible by 3 (the sum of its digits.)
When we truncate the last digit from 201, we get 20, which is a Harshad number.
When we truncate the last digit from 20, we get 2, which is also a Harshad number.
Let's call a Harshad number that, while recursively truncating the last digit, always results in a Harshad number a right truncatable Harshad number.

Also:
201/3=67 which is prime.
Let's call a Harshad number that, when divided by the sum of its digits, results in a prime a strong Harshad number.

Now take the number 2011 which is prime.
When we truncate the last digit from it we get 201, a strong Harshad number that is also right truncatable.
Let's call such primes strong, right truncatable Harshad primes.

You are given that the sum of the strong, right truncatable Harshad primes less than 10000 is 90619.

Find the sum of the strong, right truncatable Harshad primes less than 10^14.
"""
import math
import operator

from functools import reduce

from utils import harshad, prime


class Problem387(object):
    @staticmethod
    def solve(max_n=10**14):
        """Solve problem 387

        This approach builds up right truncatable harshad numbers: start
        with the two digit ones, then each iteration adds a digit.

        We need to keep track of plain ol' right truncatable harshads: that
        serves as the input for the next iteration. Then filter then down to
        just the "strong" ones. Then generate the candidate numbers from those
        capturing the prime candidates.

        This has logarithmic performance for max_n.

        :param max_n: limit, defaults to problem value: 10**14
        :return: sum of numbers adhering to problem rules
        """
        sum = 0
        digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        harshads = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for c in range(1, math.ceil(math.log10(max_n))):
            # generate next set of harshads
            harshads = [h*10+d for h in harshads for d in digits if harshad.is_harshad(h*10+d)]
            # filter down to just strong
            strongs = [h for h in harshads if harshad.is_strong_harshad(h)]
            # break if we've gone too far
            if strongs[0]*10 > max_n: break
            # assemble candidates and accumulate the prime numbers
            sum += reduce(operator.add, (s + d for s in (s * 10 for s in strongs) for d in digits if s+d < max_n and prime.is_prime(s+d)), 0)
        return sum

    @staticmethod
    def get_tests():
        return [(10**14, 696067597313468), (10000, 90619)]


if __name__ == '__main__':
    print("The answer is", Problem387.solve())
