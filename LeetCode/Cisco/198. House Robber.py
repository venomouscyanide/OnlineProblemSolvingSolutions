# https://leetcode.com/problems/house-robber/
from functools import lru_cache


class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        self.nums = nums
        tally = []

        for i in range(0, len(self.nums) - 1):
            tally.append(self.dp(i))

        return tally[0]

    @lru_cache(None)
    def dp(self, i):
        if i > len(self.nums) - 1:
            return 0
        tally = max(self.dp(i + 1), self.dp(i + 2) + self.nums[i])
        return tally


# class Solution:
#
#     def rob(self, nums) -> int:
#
#         # Special handling for empty case.
#         if not nums:
#             return 0
#
#         maxRobbedAmount = [None for _ in range(len(nums) + 1)]
#         N = len(nums)
#
#         # Base case initialization.
#         maxRobbedAmount[N], maxRobbedAmount[N - 1] = 0, nums[N - 1]
#
#         # DP table calculations.
#         for i in range(N - 2, -1, -1):
#             # Same as recursive solution.
#             maxRobbedAmount[i] = max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i])
#
#         return maxRobbedAmount[0]


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(Solution().rob(nums))

    nums = [1, 5, 35, 1]
    print(Solution().rob(nums))
