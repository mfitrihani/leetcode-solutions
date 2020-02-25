import itertools


def combinationSum3(k, n):
    return [[y for y in x] for x in itertools.combinations([i for i in range(1, 10)], k) if sum(x) == n]


if __name__ == '__main__':
    print(combinationSum3(3, 9))
