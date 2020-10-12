"""Problem 169 - Project Euler

Exploring the number of different ways a number can be expressed as a sum of powers of 2

Define f(0)=1 and f(n) to be the number of different ways n can be expressed as a sum of integer powers
of 2 using each power no more than twice.

For example, f(10)=5 since there are five different ways to express 10:

  | 1 + 1 + 8
  | 1 + 1 + 4 + 4
  | 1 + 1 + 2 + 2 + 4
  | 2 + 4 + 4
  | 2 + 8

What is f(10^25)?

---------------------------------------------------------------------------------------------------
Optimizations
 * 2^x < 10^25  => x = 83

find the solution with fewest values then use math to decompose those arguments
 | 10: [3,1]
 | 10^25 : [83, 78, 74, 72, 71, 68, 66, 64, 60, 58, 57, 52, 50, 40, 38, 35, 30, 27, 25]

Are there any patterns to this?
f(2^n) = n+1     f(1)=1, f(2)=2, f(4)=3, f(8)=4, ...
f(2^n -1) = 1    f(3)=1, f(7)=1, f(15)=1, ...

Apparently this is a thing: https://oeis.org/A002487, Stern's diatomic series.
a(0) = 0
a(1) = 1
a(2*n) = a(n)
a(2*n+1) = a(n) + a(n+1)
Note, however, that the diatomic series is off by one from f(n):
series:  0, 1, 1, 2, 1, 3, 2, 3, 1, 4, 3, 5, 2, 5, 3, 4, 1, ...
That means, in the series, 2^n=1, 2^n+1=n
"""

# seed cache with powers of 2
cache = {2**i:1 for i in range(0, 25)}


def a(n: int) -> int:
    if n in cache:
        return cache[n]
    k = n // 2
    if n % 2 == 0:
        v = a(k)
    else:
        v = a(k) + a(k+1)
    cache[n] = v
    return v


class Problem169(object):
    @staticmethod
    def solve(n=10**25):
        return a(n+1)

    @staticmethod
    def get_tests():
        return [(10, 5), (1e25, 178653872807)]


if __name__ == '__main__':
    print("The answer is", Problem169.solve())
