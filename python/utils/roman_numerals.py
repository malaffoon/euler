"""Methods for dealing with Roman Numerals
"""

_numeral_values = (
    ('M', 1000),
    ('CM', 900),
    ('D',  500),
    ('CD', 400),
    ('C',  100),
    ('XC',  90),
    ('L',   50),
    ('XL',  40),
    ('X',   10),
    ('IX',   9),
    ('V',    5),
    ('IV',   4),
    ('I',    1)
)


def toRomanNumeral(n):
    """Convert the integer value to the most efficient roman numeral"""
    result = ''
    for numeral, value in _numeral_values:
        while n >= value:
            result += numeral
            n -= value
    return result


def fromRomanNumeral(r):
    result = 0
    for numeral, value in _numeral_values:
        while r.startswith(numeral):
            result += value
            r = r[len(numeral):]
    return result
