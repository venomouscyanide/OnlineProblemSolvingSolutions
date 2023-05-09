# https://leetcode.com/problems/majority-element/description/
from collections import Counter


class Solution:
    def majorityElement(self, nums):
        common = Counter(nums).most_common(1)
        return common[0][0]
