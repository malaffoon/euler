"""Helpers for dealing with Harshad numbers

A harshad number is a number that is divisible by the sum of its digits.
NOTE: we are considering only base-10 harshad numbers.

https://en.wikipedia.org/wiki/Harshad_number
https://oeis.org/A005349

First 61 harshad numbers:
1,2,3,4,5,6,7,8,9,10,12,18,20,21,24,27,30,36,40,42,45,48,50,54,60,63,70,72,80,81,84,90,100,102,108,110,
111,112,114,117,120,126,132,133,135,140, 144,150,152,153,156,162,171,180,190,192,195,198,200,201,204

Some properties
* obviously, 10 and all powers of 10 are harshad numbers
* prime numbers greater than 10 are NOT harshad numbers
* ??? a number whose digit sum divides 9 is a harshad number
   * wiki stated this but i haven't confirmed it yet

From Problem 387, they define a "right truncatable harshad number" and a
"strong harshad nmber".
"""
from utils.prime import is_prime


def is_harshad(value):
    """A harshad number is a number that is divisible by the sum of its digits.
    NOTE: this implementation is restricted to base 10.

    Example, 201 % 3 == 0, where 3 = 2+0+1

    Harshad numbers up to 1000:
    1,2,3,4,5,6,7,8,9,10,12,18,20,21,24,27,30,36,40,42,45,48,50,54,60,63,70,72,80,81,84,90,100,102,108,110,111,112,114,117,120,126,132,133,135,140,144,150,152,153,156,162,171,180,190,192,195,198,200,201,204,207,209,210,216,220,222,224,225,228,230,234,240,243,247,252,261,264,266,270,280,285,288,300,306,308,312,315,320,322,324,330,333,336,342,351,360,364,370,372,375,378,392,396,399,400,402,405,407,408,410,414,420,423,432,440,441,444,448,450,460,465,468,476,480,481,486,500,504,506,510,511,512,513,516,518,522,531,540,550,552,555,558,576,588,592,594,600,603,605,612,621,624,629,630,640,644,645,648,660,666,684,690,700,702,704,711,715,720,730,732,735,736,738,756,770,774,777,780,782,792,800,801,803,804,810,820,825,828,832,840,846,864,870,874,880,882,888,900,902,910,912,915,918,935,936,954,960,966,972,990,999

    :param value: number to check
    :return: True if the number is a harshad number, False otherwise
    """
    return value % _sum_digits(value) == 0


def is_strong_harshad(value):
    """A strong harshad number is a harshad number where the the result of
    dividing by the sum of its digit is prime.

    Example, 201 / 3 = 67, which is prime.

    Strong harshad numbers up to 1000:
    18,21,27,42,45,63,84,111,114,117,133,152,153,156,171,190,195,198,201,207,209,222,228,247,261,266,285,333,370,372,399,402,407,423,444,465,481,511,516,518,531,555,558,592,603,629,645,666,711,730,732,738,774,777,801,803,804,846,888,915,954,999

    :param value:
    :return:
    """
    sum = _sum_digits(value)
    return value % sum == 0 and is_prime(value // sum)
    pass


def is_right_truncatable_harshad(value):
    """A right truncatable harshad number is a number that, while recursively
    truncating the last digit, always results in a harshad number.

    For example:
    201 is a Harshad number because it is divisible by 3 (the sum of its digits.)
    When we truncate the last digit from 201, we get 20, which is a Harshad number.
    When we truncate the last digit from 20, we get 2, which is also a Harshad number.

    This implementation brute forces a single value. For finding lots of such
    numbers, creating a sieve-like array or something would probably be better.

    :param value: number to test
    :return: True or False
    """
    while value >= 1:
        if not is_harshad(value): return False
        value //= 10
    return True


def _sum_digits(value):
    sum, n = 0, value
    while n:
        sum, n = sum + n % 10, n // 10
    return sum
