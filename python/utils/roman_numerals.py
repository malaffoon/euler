"""Methods for dealing with Roman Numerals
"""

_mappings = (
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
    for mapping in _mappings:
        while n >= mapping[1]:
            result += mapping[0]
            n -= mapping[1]
    return result


def fromRomanNumeral(r):
    result = 0
    for mapping in _mappings:
        while r.startswith(mapping[0]):
            result += mapping[1]
            r = r[len(mapping[0]):]
    return result
