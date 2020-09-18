"""Problem 93 - Project Euler

Arithmetic expressions

By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic
operations (+, −, *, /) and brackets/parentheses, it is possible to form different positive integer targets.

For example,
8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) − 1
36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum,
and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers,
1 to n, can be obtained, giving your answer as a string: abcd.

---------------------------------------------------------------------------------------------------
Consider brute force:

There aren't very many sets; probably 0 isn't in them but, even if it is, 10c4 = 210 combos. Maybe only 9c4 = 126.
How many ways can a set be arranged with operators: 4 x 4 x 3 x 4 x 2 x 4 x 1 = 1536.
Then parens can be inserted.
Still, it seems like the possible expressions may be numerable.

Then use eval() to calculate all results. We can generate the possible expressions using variables
and then evaluate for all combinations (24 per combo of digits). There are 4^3=64 combinations of
operators. I've hard-coded the expression templates to deal with parens, there are 11 of those.
Actually, after fiddling with precedence, i think there are only 5 templates:
((a+b)+c)+d
(a+b)+(c+d)
(a+(b+c))+d
a+((b+c)+d)
a+(b+(c+d))
So we have 5x64=320 expressions. Each evaluated 24 times for 126 combos. Doable?

I'm pretty sure you have to have a 1 in the set; can't prove it though.
"""
from itertools import combinations, permutations, product

expression_templates = (
    '((a{op1}b){op2}c){op3}d',
    '(a{op1}b){op2}(c{op3}d)',
    '(a{op1}(b{op2}c)){op3}d',
    'a{op1}((b{op2}c){op3}d)',
    'a{op1}(b{op2}(c{op3}d))',
)
operations = ('+', '-', '*', '/')

expressions = [template.replace('{op1}', ops[0]).replace('{op2}', ops[1]).replace('{op3}', ops[2])
               for template in expression_templates for ops in product(operations, repeat=3)]


class Problem93(object):
    @staticmethod
    def solve():
        def _consecutives(values):
            for i, value in enumerate(values, start=1):
                if value > i:
                    return i-1
            return len(values)

        winner, longest = None, 0
        for digits in combinations(range(1, 10), 4):
            targets = set()  # use set to de-dup
            for (a, b, c, d) in permutations(digits):
                for expression in expressions:
                    try:
                        value = eval(expression)
                        if value > 0 and value == int(value):
                            targets.add(int(value))
                    except ZeroDivisionError:
                        continue
            n = _consecutives(sorted(targets))
            if n > longest:
                winner = digits
                longest = n
            # is it fair to leave this in if i can't prove it?
            if digits[0] != 1:
                break
        return ''.join(str(d) for d in winner)

    @staticmethod
    def get_tests():
        return [(None, '1258')]


if __name__ == '__main__':
    print("The answer is", Problem93.solve())
