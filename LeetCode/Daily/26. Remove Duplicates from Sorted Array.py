# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# class Solution:
#     def removeDuplicates(self, nums):
#         if not nums:
#             return 0
#
#         if len(nums) == 1:
#             return 1
#
#         next_index = 1
#         prev_index = 0
#         upper_limit = len(nums)
#         while next_index < upper_limit:
#             if nums[prev_index] == nums[next_index]:
#                 for i in range(prev_index, len(nums) - 1):
#                     nums[i] = nums[i + 1]
#                 upper_limit -= 1
#             else:
#                 prev_index += 1
#                 next_index += 1
#         return upper_limit


class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        left = 0
        right = 1

        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
                right += 1

        return left + 1


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    Solution().removeDuplicates(nums)
    print(nums)

    nums = [1, 1, 2]
    Solution().removeDuplicates(nums)
    print(nums)
