def subsets(nums):
    res = [[]]
    for n in nums:
        res += [i + [n] for i in res]
    return res


if __name__ == '__main__':
    print(subsets([1, 2, 3]))
