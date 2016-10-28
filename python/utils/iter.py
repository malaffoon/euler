"""More iterable utils
"""
from itertools import islice


def slide(seq, n=2):
    """Generator for sliding tuples of width n over an string or iterable"""
    if isinstance(seq, str):
        yield from (seq[i:i+n] for i in range(len(seq)-n+1))
    else:
        it = iter(seq)
        w = tuple(islice(it, n))
        if len(w) == n:
            yield w
        for i in it:
            w = w[1:] + (i,)
            yield w


def rotations(v):
    """Returns a tuple of rotations of a value.

    If the value is a string it is rotated, returning strings:
      rotations('abc') -> ('abc', 'bca', 'cab')
    If the value is an int, it is rotated, returning ints:
      rotations(123) -> (123, 231, 312)
    If the value is sliceable its values are rotated, returning tuples of the values:
      rotations(range(1,4)) -> ((1,2,3,4), (2,3,4,1), (3,4,1,2), (4,1,2,3))
    Otherwise, str(v) is rotated.
    """
    seq, func = v, lambda x: x
    if isinstance(v, str):
        pass
    elif isinstance(v, int):
        seq, func = str(v), int
    elif hasattr(v, "__iter__"):
        seq = tuple(v)
    else:
        seq = str(v)
    return (func(seq[i:]+seq[:i]) for i in range(0, len(seq)))
