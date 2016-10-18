"""Problem 26 - Project Euler

Reciprocal cycles

A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10 are given:
  | 1/2	= 	0.5
  | 1/3	= 	0.(3)
  | 1/4	= 	0.25
  | 1/5	= 	0.2
  | 1/6	= 	0.1(6)
  | 1/7	= 	0.(142857)
  | 1/8	= 	0.125
  | 1/9	= 	0.(1)
  | 1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""


class Problem26(object):
    @staticmethod
    def solve(limit=1000):

        def cycle_length(n):
            """Use long-division technique to count cycle length

            For example, for 7 (1/7):
                seen -> [10,40,20,80,50,70] then val -> 10 and length = 6-0 = 6
            For example, for 6 (1/6):
                seen -> [10,40] then val -> 40 and length = 2-1 = 1
            """
            seen = [10]
            for _ in range(0, n):
                val = 10 * (seen[-1] % n)
                if val == 0:
                    return 0
                if val in seen:
                    return len(seen) - seen.index(val)
                seen.append(val)
            return None

        return max(((d, cycle_length(d)) for d in range(2, limit)), key=lambda x: x[1])[0]

    @staticmethod
    def get_tests():
        return [(1000, 983), (10, 7), (100, 97)]


if __name__ == '__main__':
    print("The answer is", Problem26.solve())
