# https://leetcode.com/problems/burst-balloons/
from functools import lru_cache


class Solution:
    def maxCoins(self, nums):

        nums = [1] + nums + [1]
        cache = [[0 for i in range(len(nums))] for _ in range(len(nums))]

        def dfs(l, r):
            if l > r:
                return 0

            val = cache[l][r]
            if val:
                return val

            for i in range(l, r + 1):
                a = nums[l - 1] * nums[i] * nums[r + 1]
                b = dfs(l, i - 1)
                c = dfs(i + 1, r)
                value = a + b + c
                cache[l][r] = max(cache[l][r], value)
            return cache[l][r]

        return dfs(1, len(nums) - 2)


if __name__ == '__main__':
    nums = [3, 1, 5, 8]
    print(Solution().maxCoins(nums))
