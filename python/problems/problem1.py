"""Problem 1 - Project Euler

   Multiples of 3 and 5:

   If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
   The sum of these multiples is 23.

   Find the sum of all the multiples of 3 or 5 below 1000.
"""


class Problem1(object):
    def solve(self, limit=1000):
        """Find the sum of all the multiples of 3 or 5 below the limit"""
        return self.solution2(limit)

    def get_tests(self):
        return [(1000, 233168), (10, 23)]

    @staticmethod
    def solution1(limit=1000):
        """Get array of multiples of 3 or 5, then sum them"""
        return sum(filter(lambda n: n % 3 == 0 or n % 5 == 0, range(1, limit)))

    @staticmethod
    def solution2(limit=1000):
        """Loop through numbers, adding to sum"""
        answer = 0
        for n in range(1, limit):
            if n % 3 == 0 or n % 5 == 0: answer += n
        return answer


if __name__ == '__main__':
    print("The sum of all the multiples of 3 or 5 below 1000 is", Problem1().solve(1000))
