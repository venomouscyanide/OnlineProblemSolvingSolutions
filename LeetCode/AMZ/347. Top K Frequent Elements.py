# https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        counter = Counter(nums)
        return list(map(lambda x: x[0], counter.most_common(k)))


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2

    print(Solution().topKFrequent(nums, k))
