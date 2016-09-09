import timeit
import cProfile

from problems.problem7 import Problem7


if __name__ == '__main__':
    N = 100
    print(timeit.timeit('Problem7.solve()', setup='from problems.problem7 import Problem7', number=N) / N)

    def profile_solve():
        for _ in range(N): Problem7.solve()
    cProfile.run('profile_solve()')

"""Results
timeit result is 6.0ms per call

Output of cProfile::
         1001104 function calls in 0.703 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.703    0.703 <string>:1(<module>)
        1    0.000    0.000    0.703    0.703 perf_problem7.py:11(profile_solve)
      100    0.000    0.000    0.000    0.000 prime.py:12(ensure_sieve)
      100    0.089    0.001    0.703    0.007 prime.py:43(nth)
      100    0.001    0.000    0.001    0.000 prime.py:50(guess_limit)
  1000200    0.613    0.000    0.613    0.000 prime.py:55(generator)
      100    0.000    0.000    0.703    0.007 problem7.py:14(solve)
        1    0.000    0.000    0.703    0.703 {built-in method builtins.exec}
      100    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      100    0.000    0.000    0.000    0.000 {built-in method math.ceil}
      300    0.000    0.000    0.000    0.000 {built-in method math.log}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""



