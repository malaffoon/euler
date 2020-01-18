from itertools import count
from math import gcd


def generator(limit: int = None, primitive: bool = True):
    """Generator for Pythagorean triples.

    A Pythagorean triple consists of three positive integers a, b, c such that
    a^2 + b^2 = c^2. A well-known example is (3,4,5). A primitive Pythagorean
    triple is one in which a,b,c are co-prime (i.e. no common divisor larger
    than 1).

    If a limit is given, the generator will return only those triples whose
    sum of a+b+c doesn't exceed the limit. If the primitive flag is set True
    only primitive triples will be returned.

    You must specify either a limit or the primitive flag.

    Note: the triples aren't in any particular order although they generally
    go from small to large. The triple tuple is also not orders; i.e. it may
    return (3,4,5) or (5,3,4).

    :param limit: optional, maximum sum of a+b+c
    :param primitive: True to return only primitive triples
    :return: sequence of triples, (a,b,c)
    """
    if not limit and not primitive:
        raise ValueError("Please provide a limit when generating non-primitive triples")

    # Use Euclid's formula to generate primitive triples
    for m in count(2):
        if limit and 2 * m * (m + 1) > limit: break
        for n in range(1 if m % 2 == 0 else 2, m, 2):
            s = 2 * m * (m + n)
            if limit and s > limit: break
            if gcd(m, n) != 1: continue
            a, b, c = m*m-n*n, 2*m*n, m*m+n*n
            yield a, b, c
            if not primitive:
                for k in range(2, limit // s):
                    yield k*a, k*b, k*c


if __name__ == '__main__':
    print(f"Primitive triples up to 108: {list(generator(108, True))}")
    print(f"All triples up to 108: {list(generator(108, False))}")
