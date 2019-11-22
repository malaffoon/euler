import cProfile

from utils.collatz import next_collatz, generator, length

def gen(n):
    result = []
    while n:
        result.append(n)
        n = None if n == 1 else int(n/2) if n % 2 == 0 else 3 * n + 1
    return result

def test():
    for i in range(50000, 100001):
        # length = sum(1 for _ in generator(i))
        # length = len(gen(i))
        l = length(i)

if __name__ == '__main__':
    cProfile.run('test()')


