"""Problem 68 - Project Euler

Magic 5-gon ring

Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.


Working clockwise, and starting from the group of three with the numerically lowest external node
(4,3,2 in this example), each solution can be described uniquely. For example, the above solution
can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6
By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings.
What is the maximum 16-digit string for a "magic" 5-gon ring?


Just gonna brute force this one, there aren't that many permutations ...
"""
import itertools


class Problem68(object):
    @staticmethod
    def solve(n=5):
        return Problem68.solve3() if n == 3 else Problem68.solve5()

    @staticmethod
    def solve3():
        solutions = set()
        numbers = tuple(range(1, 6+1))
        min_sum, max_sum = 9, 12
        for c1 in itertools.permutations(numbers, 3):
            cur_sum = sum(c1)
            if cur_sum < min_sum or cur_sum > max_sum: continue;
            n2 = [n for n in numbers if n not in c1]
            for c2 in ((combo[0], c1[2], combo[1]) for combo in itertools.permutations(n2, 2)):
                if sum(c2) != cur_sum: continue
                for c3 in ((n, c2[2], c1[1]) for n in n2 if n not in c2):
                    if sum(c3) != cur_sum: continue
                    # rotate tuple so lowest external value is first
                    solution = [c1, c2, c3]
                    idx = sorted(enumerate(solution), key=lambda e: e[1][0])[0][0]
                    solution = tuple(solution[idx:] + solution[:idx])
                    if solution not in solutions:
                        solutions.add(solution)
        return max(int(''.join(str(n) for group in solution for n in group)) for solution in solutions)

    @staticmethod
    def solve5():
        solutions = set()
        numbers = tuple(range(1, 11))
        min_sum, max_sum = 14, 19
        for c1 in itertools.permutations(numbers, 3):
            cur_sum = sum(c1)
            if cur_sum < min_sum or cur_sum > max_sum: continue
            if 10 in c1[1:]: continue
            n2 = [n for n in numbers if n not in c1]
            for c2 in ((combo[0], c1[2], combo[1]) for combo in itertools.permutations(n2, 2)):
                if sum(c2) != cur_sum: continue
                if 10 in c2[1:]: continue
                n3 = [n for n in n2 if n not in c2]
                for c3 in ((combo[0], c2[2], combo[1]) for combo in itertools.permutations(n3, 2)):
                    if sum(c3) != cur_sum: continue
                    if 10 in c3[1:]: continue
                    n4 = [n for n in n3 if n not in c3]
                    for c4 in ((combo[0], c3[2], combo[1]) for combo in itertools.permutations(n4, 2)):
                        if sum(c4) != cur_sum: continue
                        if 10 in c4[1:]: continue
                        for c5 in ((n, c4[2], c1[1]) for n in n4 if n not in c4):
                            if sum(c5) != cur_sum: continue
                            if 10 in c5[1:]: continue
                            # rotate tuple so lowest external value is first
                            solution = [c1, c2, c3, c4, c5]
                            idx = sorted(enumerate(solution), key=lambda e: e[1][0])[0][0]
                            solution = tuple(solution[idx:] + solution[:idx])
                            if solution not in solutions:
                                solutions.add(solution)
        return max(int(''.join(str(n) for group in solution for n in group)) for solution in solutions)


    @staticmethod
    def get_tests():
        return [(None, 6531031914842725)]


if __name__ == '__main__':
    print("The answer is", Problem68.solve())
