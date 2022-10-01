# https://leetcode.com/problems/maximum-subarray/
def run(nums):
    # studied and applied kadane's algo
    maximum = nums[0]
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] = nums[i] + nums[i - 1]
        if nums[i] > maximum:
            maximum = nums[i]
    return maximum


def run_non_opt(nums):
    # not optimized, Passes only 200/209
    lp = 1

    if len(nums) == 1:
        return nums[0]

    running_sum = nums[0]

    tot = len(nums)
    prev = 0

    outer_best = nums[prev]
    inner_best = nums[prev]
    while lp < tot:
        current = nums[lp] + running_sum
        if current > inner_best:
            inner_best = current
        running_sum = current

        lp += 1
        if lp == tot:
            lp = prev + 1
            prev = lp
            running_sum = nums[lp]
            if inner_best > outer_best:
                outer_best = inner_best
            inner_best = nums[lp]
            lp += 1

    if outer_best < nums[-1]:
        outer_best = nums[-1]
    return outer_best


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(run(nums))

    nums = [5, 4, -1, 7, 8]
    print(run(nums))

    nums = [-2, 1]
    print(run(nums))

    nums = [-1, -2]
    print(run(nums))

    nums = [-2, -3, -1]
    print(run(nums))
