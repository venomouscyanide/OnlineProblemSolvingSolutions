# https://leetcode.com/problems/find-the-duplicate-number/
import collections
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        return counter.most_common()[0][0]
