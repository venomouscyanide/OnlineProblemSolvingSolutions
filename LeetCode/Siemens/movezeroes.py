from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counter = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                to_insert = nums.pop(i)
                nums.insert(counter, to_insert)
                counter += 1


if __name__ == '__main__':
    nums = [0, 0, 1, 0, 1, 111, 23, 43, 0]
    Solution().moveZeroes(nums)
    print(nums)
