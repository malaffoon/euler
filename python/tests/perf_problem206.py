import cProfile

from problems.problem206 import Problem206

# The initial solution using regex was easy and obvious but i was sure that all
# those string manipulations and regex would be slower than using math. I was
# wrong. Removing the inconsequential setup and framework calls:
"""
solve_regex
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1   15.315   15.315   25.641   25.641 problem206.py:20(solve_regex)
 37891817   10.326    0.000   10.326    0.000 {method 'match' of '_sre.SRE_Pattern' objects}

solve_divmod
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    8.318    8.318   43.044   43.044 problem206.py:31(solve_divmod)
 37892562   24.946    0.000   34.726    0.000 problem206.py:33(_has_form)
 75785124    9.780    0.000    9.780    0.000 {built-in method builtins.divmod}
"""

# Using the python slice trick instead of regex improves things a teeny bit:
"""
solve_slice
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1   14.989   14.989   14.989   14.989 problem206.py:48(solve_slice)
"""

# Constraining the values to end in '30'/'70' and using the slice trick:
"""
solve_skip
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    4.062    4.062    4.062    4.062 problem206.py:59(solve_goofy)
"""


def run_solve():
    Problem206().solve_best()


if __name__ == '__main__':
    # print("no timing/profiling is run automatically")
    # time_problem1()
    cProfile.run('run_solve()')


