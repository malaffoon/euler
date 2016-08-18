"""Utilities for Fibonacci sequence
   There is both an iterator object, Fibonacci, and a generator, fibgen.
   They both lazily generate the values.

   >>> from utils.fibonacci import Fibonacci
   >>> list(Fibonacci())
   [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

   >>> from utils.fibonacci import fibgen
   >>> list(fibgen(max_value=10))
   [1, 1, 2, 3, 5, 8]
"""

from itertools import islice


class Fibonacci(object):
    """An iterator for Fibonacci sequence"""
    def __init__(self, max_value=None, max_count=10):
        if max_value is None and max_count is None:
            raise ValueError('Either value or count must have a limit set')
        self.max_value = max_value
        self.max_count = max_count

    def __iter__(self):
        self.count = 0
        self.prev = 0
        self.curr = 1
        return self

    def __next__(self):
        if self.max_value is not None and self.curr > self.max_value:
            raise StopIteration
        if self.max_count is not None and self.count >= self.max_count:
            raise StopIteration
        self.count += 1
        self.prev, self.curr = self.curr, self.prev+self.curr
        return self.prev
    next = __next__  # p2 compatibility


def fibgen(max_value=None, max_count=10):
    """A python generator for Fibonacci sequence"""
    if max_value is None and max_count is None:
        raise ValueError('Either value or count must have a limit set')
    count = 0
    prev,curr = 0,1
    while (max_value is None or curr <= max_value) and (max_count is None or count < max_count):
        yield curr
        count += 1
        prev, curr = curr, prev+curr

def fibn(n):
    """Return nth Fibonacci number; 1-based"""
    return islice(fibgen(max_count=n), n-1, n).__next__()
