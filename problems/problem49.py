"""Problem 49 - Project Euler

   Prime permutations

   The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
   (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

   There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
   but there is one other 4-digit increasing sequence.

   What 12-digit number do you form by concatenating the three terms in this sequence?
"""

import itertools

from utils import prime


class Problem49(object):
    @staticmethod
    def solve():
        # get the two sequences, and return the second one concatenated
        return ''.join(str(n) for n in find_sequences()[1])


def find_sequences():
    sequences = []
    # go through all 4-digit primes, gathering sorted, unique prime permutations
    for perms in (clean_permutations(get_permutations(p)) for p in prime.generator(10000) if p > 999):
        if len(perms) < 3: continue
        # find trios of the values that have the same difference between first/middle/last values
        for trio in itertools.combinations(perms, 3):
            if trio[1]-trio[0] == trio[2]-trio[1] and trio not in sequences:
                sequences.append(trio)
    return sequences


def get_permutations(n):
    """ Return permutations of the given number
        The number will be the first in the list; otherwise unsorted.
          get_permutations(1478) = [1478, 1487, 1748, 1784, 1847, 1874, 4178, 4187, 4718, 4781, 4817, 4871, 7148, 7184, 7418, 7481, 7814, 7841, 8147, 8174, 8417, 8471, 8714, 8741]
    """
    perms = [n]
    for c in itertools.permutations(str(n)):
        p = int(''.join(c))
        if p not in perms:
            perms.append(p)
    return perms


def clean_permutations(perms):
    """ Remove permutations that are less than initial value
        Remove permutations that are not prime
        Sort remaining permutations in ascending order
          clean_permutations(get_permutations(1478)) = [1487, 1847, 4817, 4871, 7481, 7841, 8147, 8741]
    """
    return sorted([p for p in perms if p >= perms[0] and prime.is_prime(p)])


if __name__ == '__main__':
    print("The answer is", Problem49().solve())
