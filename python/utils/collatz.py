"""Helpers for dealing with Collatz sequences
"""

import collections


def next_collatz(n):
    """Return the next Collatz number
       Returns None for n == 1 (to avoid infinitely looping [4,2,1])
    """
    return None if n == 1 else int(n/2) if n % 2 == 0 else 3 * n + 1


def generator(value):
    """Return the Collatz sequence for a number"""
    while value:
        yield value
        value = next_collatz(value)


def length(n):
    """Return length of the Collatz sequence for a number"""
    result = 0
    while n:
        result += 1
        n = None if n == 1 else int(n/2) if n % 2 == 0 else 3 * n + 1
    return result


def reverse(limit):
    """Reverse-generate collatz sequences.

       Result is a list of lists where the longest lists have length=limit.
       The last value in each list is the number for which that list is the reverse collatz sequence.
         reverse(6) = [[1,2,4], [1,2,4,8], [1,2,4,8,16], [1,2,4,8,16,5], [1,2,4,8,16,32]]

       This isn't really tenable, the number of lists explodes pretty quick
    """
    # deque of lists that need to be extended
    work = collections.deque()

    # initialization of first three is easy
    result = [[1,2,4],[1,2,4,8],[1,2,4,8,16]]
    work.append(result[-1])

    while True:
        lst = work.popleft()
        if len(lst) >= limit:
            break
        n = lst[-1]
        odd = (n-1)/3
        if odd == int(odd):
            oddlst = lst[:] + [int(odd)]
            work.append(oddlst)
            result.append(oddlst)
        evenlst = lst[:] + [int(2*n)]
        work.append(evenlst)
        result.append(evenlst)
    return result
