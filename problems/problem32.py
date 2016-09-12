"""Problem 32 - Project Euler

Pandigital products

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product
is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""


class Problem32(object):
    @staticmethod
    def solve():
        def distinct_valid_digits(digits):
            valid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            return all(d in valid and digits.count(d) == 1 for d in digits)

        def valid_multiplier(n):
            return distinct_valid_digits(str(n))

        def valid_solution(a, b, p):
            digits = ''.join((str(arg) for arg in [a, b, p]))
            return len(digits) == 9 and distinct_valid_digits(digits)

        products = set()  # de-dup using a set
        for a in (d for d in range(1, 10000) if valid_multiplier(d)):
            for b in (d for d in range(a + 1, 10000) if valid_multiplier(d)):
                p = a * b
                if p > 10000:
                    break
                if valid_solution(a, b, p):
                    products.add(p)
        return sum(products)


if __name__ == '__main__':
    print("The answer is", Problem32.solve())
