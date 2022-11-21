# https://leetcode.com/problems/wiggle-sort/


class Solution:
    def wiggleSort(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        elements = len(nums)
        half_way = elements // 2
        low_high = sorted(nums)[:half_way]

        if elements % 2 == 0:
            high_low = sorted(nums, reverse=True)[:half_way]
        else:
            high_low = sorted(nums, reverse=True)[:half_way + 1]

        if elements % 2 == 0:
            upper = elements
        else:
            upper = elements - 1

        for index in range(upper):
            if index % 2 == 0:
                nums[index] = low_high.pop(0)
            else:
                nums[index] = high_low.pop(0)

        if upper != elements:
            nums[-1] = high_low.pop()


if __name__ == '__main__':
    nums = [3, 5, 2, 1, 6, 4]
    Solution().wiggleSort(nums)
    print(nums)

    nums = [0]
    Solution().wiggleSort(nums)
    print(nums)
