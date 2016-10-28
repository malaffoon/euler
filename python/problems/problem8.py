"""Problem 8 - Project Euler

Largest product in a series.

The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

  | 73167176531330624919225119674426574742355349194934...

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
What is the value of this product?
"""

from functools import reduce
import operator

PROBLEM8_DATA = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"


class Problem8(object):
    @staticmethod
    def solve0(n=13):
        # ignore 0's: 1.7ms
        digits = [int(s) for s in PROBLEM8_DATA]
        return max(reduce(operator.mul, seg, 1) for seg in
                   map(lambda i: digits[i:i + n], range(0, len(digits) - n)))

    @staticmethod
    def solve(n=13):
        # advance slowly past 0's: 1.0ms
        digits = [int(s) for s in PROBLEM8_DATA]
        return max(reduce(operator.mul, seg, 1) for seg in
                   map(lambda i: digits[i:i + n], range(0, len(digits) - n)) if 0 not in seg)

    @staticmethod
    def solve3(n=13):
        # advance aggressively past 0's: 0.90ms
        digits = [int(s) for s in PROBLEM8_DATA]
        i = 0
        result = 0
        while i + n < len(digits):
            if digits[i + n - 1] == 0:
                i += n
                continue
            result = max(result, reduce(operator.mul, digits[i:i + n], 1))
            i += 1
        return result

    @staticmethod
    def get_tests():
        return [(13, 23514624000), (4, 5832)]


if __name__ == '__main__':
    print("The answer is", Problem8.solve())
