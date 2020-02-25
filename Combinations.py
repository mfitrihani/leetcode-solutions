from itertools import combinations


def combine(n, k):
    return [[y for y in x] for x in combinations([i for i in range(1, n + 1)], k)]


if __name__ == '__main__':
    print(combine(4, 2))
