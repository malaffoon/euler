"""Problem 112 - Project Euler

Bouncy numbers

Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below
one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first
reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of
bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.

---------------------------------------------------------------------------------------------------

Played around with patterns; pretty sure there is an algebraic solution.
But, brute-force works and doesn't take too long.

Oh, but problem 113 is going to make me revisit things. Hmm.

"""
import itertools


class Problem112(object):
    @staticmethod
    def solve(percent_bouncy):
        bouncy = 0
        for n in itertools.count(100):
            flag = 0
            s = str(n)
            for i, d in enumerate(s):
                if i == 0: continue
                if s[i] > s[i-1]: flag |= 1
                elif s[i] < s[i-1]: flag |= 2
            if flag == 3: bouncy += 1
            if 100 * bouncy / n >= percent_bouncy:
                return n
        return None

    @staticmethod
    def get_tests():
        return [(50, 538), (90, 21780), (99, 1587000)]
    

if __name__ == '__main__':
    print("The answer is", Problem112.solve(99))
