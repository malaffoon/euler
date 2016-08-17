import timeit
import cProfile

from problems.problem1 import Problem1

# Performance:
# solution2 is faster than solution1 when limit=100 (.18 vs .30)
# solution2 is faster than solution1 when limit=1000 (1.85 vs 2.86)
# solution2 is faster than solution1 when limit=5000 (9.32 vs 14.1)
#
# It is disappointing but solution2, less 'elegant', is faster.


def time_problem1():
    print(timeit.timeit('Problem1().solution1(100)', setup='from problems.problem1 import Problem1', number=10000))
    print(timeit.timeit('Problem1().solution2(100)', setup='from problems.problem1 import Problem1', number=10000))

def run_solution():
    solver = Problem1()
    for _ in range(10000): solver.solution2(1000)


if __name__ == '__main__':
    print("no timing/profiling is run automatically")
    # time_problem1()
    # cProfile.run('run_solution()')

