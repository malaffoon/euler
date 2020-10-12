"""Problem 692 - Project Euler

Siegbert and Jo

Siegbert and Jo take turns playing a game with a heap of N pebbles:
1. Siegbert is the first to take some pebbles. He can take as many pebbles as he wants. (Between 1 and N inclusive.)
2. In each of the following turns the current player must take at least one pebble and at most twice the amount of 
pebbles taken by the previous player.
3. The player who takes the last pebble wins.
Although Siegbert can always win by taking all the pebbles on his first turn, to make the game more interesting 
he chooses to take the smallest number of pebbles that guarantees he will still win 
(assuming both Siegbert and Jo play optimally for the rest of the game).

Let H(N) be that minimal amount for a heap of N pebbles.
H(1)=1, H(4)=1, H(17)=1, H(8)=8 and H(18)=5.

Let G(n) be SUM{k=1..n}(H(k))
G(13) = 43

Find G(23416728348467685) 
---------------------------------------------------------------------------------------------------
Is there a pattern or known sequence?
H(N) = 1, 2, 3, 1, 5, 1, 2, 8, 1

Appears to be https://oeis.org/A139764.
a(n) = n if n is a Fibonacci number, a(n-F0) where F0 is the largest Fibonacci number < n

fibs: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987

The number given is a teeny bit less than the 80th fibonacci number, 23416728348467744.
Presumably they did that on purpose. The 79th fibonacci number is 14472334024676260. Which
means we would need to memoize up to 8944394323791425 (23416728348467685 - 14472334024676260).
Ugh.

Perhaps there is a pattern to the sums?
The series between fib numbers seems to repeat. For example, between 21 and 34, the series
is the series below 13; between 55 and 89, the series is below 34.
We can recursively calculate the sum up to fibonacci values.
G(f) = G(f-1) + G(f-2) - (f-2) + f
G(89) = G(55) + G(34)-34 + 89
Then we can subtract out the extra 23416728348467744 - 23416728348467685 = 59 terms
"""
from utils.fibonacci import fibgen
from functools import reduce


class Problem692(object):
    @staticmethod
    def solve(n=23416728348467685):
        # generate fibs to first fib greater than n
        # oh, and get rid of first fib (the repeated 1)
        fibs = list(fibgen(max_value=n, max_count=None))[1:]
        if fibs[-1] < n:
            fibs.append(fibs[-1]+fibs[-2])

        # calculate the sum, G(n), for each fib
        fibsums = [(1, 1), (2, 3)]
        for i, f in enumerate(fibs[2:], start=2):
            s = fibsums[i-1][1] + fibsums[i-2][1] - fibsums[i-2][0] + f
            fibsums.append((f, s))

        # memoizing helper to calculate residual H's
        cache = {1: 1, 2: 2, 3: 3}
        def H(n):
            if n in cache:
                return cache[n]
            f = next(f for f in fibs[::-1] if f <= n)
            if f == n:
                return f
            h = H(n-f)
            cache[n] = h
            return h

        # last fib sum should be greater than n; subtract residual H's
        f, s = fibsums[-1]
        for i in range(n, f, -1):
            s -= H(i)

        return s

    @staticmethod
    def get_tests():
        return [(13, 43), (23416728348467685, 842043391019219959)]


if __name__ == '__main__':
    print("The answer is", Problem692.solve())
