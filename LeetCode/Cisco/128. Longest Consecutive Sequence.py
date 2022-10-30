# https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()

        overall_seq = 1
        curr_seq = 1
        prev = nums[0]
        for i in range(1, len(nums), 1):
            if nums[i] - prev == 1:
                curr_seq += 1
            else:
                overall_seq = max(curr_seq, overall_seq)
                curr_seq = 1
            prev = nums[i]
        overall_seq = max(curr_seq, overall_seq)
        return overall_seq


if __name__ == '__main__':
    nums = [1, 2, 0, 1]
    print(Solution().longestConsecutive(nums))
