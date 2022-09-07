# https://leetcode.com/problems/running-sum-of-1d-array/


def run(nums):
    if not nums:
        return nums

    sum_so_far = nums[0]

    for index, item in enumerate(nums[1:]):
        nums[index] = sum_so_far
        sum_so_far += item
    if len(nums) > 1:
        nums[index + 1] = sum_so_far

    return nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    run(nums)

    nums = [1]
    run(nums)

    nums = [1, 2, 3]
    run(nums)

    nums = []
    run(nums)
