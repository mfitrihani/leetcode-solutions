from collections import Counter
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)


if __name__ == '__main__':
    print(Solution.topKFrequent(Solution, [1, 1, 2, 3], 2))
