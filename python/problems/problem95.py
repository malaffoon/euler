""" Problem 95 - Project Euler

Amicable chains

The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors
of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220,
forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.

Algorithm
 * brute force (with memoizing) gets it done, but it takes 30 seconds
 * of course, the answer is found very quickly since 5916 is a precursor for it
"""

from utils.prime import divisors, primes


class Problem95(object):
    @staticmethod
    def solve():
        limit = 1000000
        visited = [False] * limit
        visited[0] = visited[1] = visited[2] = True
        for p in primes(limit): visited[p] = True

        longest = []
        for n in range(0, limit):
            if visited[n]: continue

            c = n
            chain = [c]
            while True:
                c = sum(proper_divisors(c))
                if c >= limit or visited[c]:
                    break
                if c in chain:
                    # actual chain is just the part that loops, don't include any precursor values in 'longest'
                    i = chain.index(c)
                    if len(chain)-i > len(longest):
                        longest = chain[i:]
                        # print(n, longest)
                    break
                chain.append(c)
            for c in chain:
                visited[c] = True
        return min(longest)

    @staticmethod
    def get_tests():
        return [(None, 14316)]


def proper_divisors(n):
    """Proper divisors do not include the number itself"""
    return divisors(n)[0:-1]


if __name__ == '__main__':
    print("The answer is", Problem95().solve())
