# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        return -1


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = -5
    print(Solution().search(nums, target))
