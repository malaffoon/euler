"""More iterable utils
"""
from itertools import islice


def slide(seq, n=2):
    """Returns a sliding tuple of width n over an iterable"""
    it = iter(seq)
    w = tuple(islice(it, n))
    if len(w) == n:
        yield w
    for i in it:
        w = w[1:] + (i,)
        yield w
