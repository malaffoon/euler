"""Problem 206 - Project Euler

Concealed Square

Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.

Obvious constraints:
 - range 1010101010 - 1389026623
 - ends in 0

See perf_problem206 for more details on performance.
"""
from math import sqrt


class Problem206(object):
    @staticmethod
    def solve():
        return Problem206.solve_best()

    @staticmethod
    def solve_regex():
        from re import compile
        form = compile('1.2.3.4.5.6.7.8.9.0')
        min_value = int(sqrt(1020304050607080900))
        max_value = int(sqrt(1929394959697989990))
        for value in range(min_value, max_value + 1, 10):
            if form.match(str(value * value)):
                return value
        return None

    @staticmethod
    def solve_divmod():
        def _has_form(v: int):
            (v, m) = divmod(v, 10)
            if m != 0: return False
            for d in (9, 8, 7, 6, 5, 4, 3, 2, 1):
                (v, m) = divmod(int(v / 10), 10)
                if m != d: return False
            return v == 0

        min_value = int(sqrt(1020304050607080900))
        max_value = int(sqrt(1929394959697989990))
        for value in range(min_value, max_value + 1, 10):
            if _has_form(value * value):
                return value
        return None

    @staticmethod
    def solve_slice():
        """Use python slice instead of regex
        """
        min_value = int(sqrt(1020304050607080900))
        max_value = int(sqrt(1929394959697989990))
        for value in range(min_value, max_value + 1, 10):
            if str(value * value)[::2] == '1234567890':
                return value
        return None

    @staticmethod
    def solve_skip():
        """Constrain values to end in '30' or '70' and use slice trick instead of regex
        """
        value = 1010101030
        while value < 1389026623:
            if str(value * value)[::2] == '1234567890':
                return value
            value += (40 if value % 100 == 30 else 60)
        return None

    @staticmethod
    def solve_best():
        """Start at maximum value instead of minimum
        """
        value = 1389026630
        while value > 1010101010:
            if str(value * value)[::2] == '1234567890':
                return value
            value -= (60 if value % 100 == 30 else 40)
        return None

    @staticmethod
    def get_tests():
        # 1389019170 ^ 2 = 1929374254627488900
        return [(None, 1389019170)]


if __name__ == '__main__':
    print("The answer is", Problem206.solve())
