""" Problem 19 - Project Euler

You are given the following information, but you may prefer to do some research for yourself.

| 1 Jan 1900 was a Monday.
| Thirty days has September,
| April, June and November.
| All the rest have thirty-one,
| Saving February alone,
| Which has twenty-eight, rain or shine.
| And on leap years, twenty-nine.
| A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

from datetime import date
import timeit

class Problem19(object):
    @staticmethod
    def solve():
        # brute force method ...
        count = 0
        for year in range(1901, 2001):
            for month in range(1, 13):
                if date(year, month, 1).weekday() == 6:
                    count += 1
        return count

    @staticmethod
    def solve2():
        # advance and check
        DAYS_PER_MONTH = [31,28,31,30,31,30,31,31,30,31,30,31]
        count = 0
        day = 0 + 365%7  # 1 Jan 1900 is Monday so this is 1 Jan 1901
        for year in range(1901, 2001):
            DAYS_PER_MONTH[1] = 29 if is_leap(year) else 28
            for m in range(12):
                if day == 6: count += 1
                day = (day + DAYS_PER_MONTH[m]) % 7
        return count

    @staticmethod
    def get_tests():
        return [(None, 171)]


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if __name__ == '__main__':
    print("The number of Sundays that fell on the first of the month is", Problem19().solve())

    # solve2 is about 30% faster (26 vs 38)
    # but solve2 is obviously a bit more brittle
    print(timeit.timeit('Problem19().solve()', setup='from problems.problem19 import Problem19', number=1000))
    print(timeit.timeit('Problem19().solve2()', setup='from problems.problem19 import Problem19', number=1000))