"""Problem 97 - Project Euler

Large non-Mersenne prime

The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form
2^6972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2^p−1, have been
found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×2^7830457+1.

Find the last ten digits of this prime number.

Algorithm
The interwebs tell me that the last m digits of a power of 2 are taken mod 10^m and have a cycle with a period
of 4x5^(m-1) starting at 2^m. For example, m=2 has a period of 20 starting at 2^2, i.e. 04. To calculate the last
two digits of any power of 2, simple mod the power with 20 to reduce the calculation. 2^52 = 2^40x2^12; 2^12 ends
with 96 so 2^52 ends with 96. For this problem:
  | m = 10
  | cycle has period 7812500, starting with 2^10 (0000001024)
  | 7830457 mod 7812500 = 17957
So, we can deal with 2^17957 which python has no trouble with
"""


class Problem97(object):
    @staticmethod
    def solve():
        return (28433 * pow(2, 7830457 % 7812500) + 1) % pow(10, 10)

    @staticmethod
    def get_tests():
        return [(None, 8739992577)]


if __name__ == '__main__':
    print("The answer is", Problem97.solve())
