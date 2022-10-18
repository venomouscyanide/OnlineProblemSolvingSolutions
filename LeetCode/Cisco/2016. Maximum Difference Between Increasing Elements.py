# https://leetcode.com/problems/maximum-difference-between-increasing-elements/
def run(nums):
    lp = 0
    rp = lp + 1

    maximum_diff = -1
    while rp < len(nums):
        if nums[rp] > nums[lp]:
            maximum_diff = max(maximum_diff, nums[rp] - nums[lp])
        else:
            lp = rp
        rp += 1

    return maximum_diff


if __name__ == '__main__':
    nums = [7, 1, 5, 4]
    print(run(nums))

    nums = [1, 2, 3, 4]
    print(run(nums))

    nums = [1, 1, 1, 1]
    print(run(nums))

    nums = [5, 4, 3, 2]
    print(run(nums))

    nums = [1, 5, 2, 10]
    print(run(nums))
