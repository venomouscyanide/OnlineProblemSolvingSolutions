# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

def run(nums):
    lp = 0
    rp = len(nums) - 1

    while lp < rp:
        if nums[lp] > nums[lp + 1]:
            return nums[lp + 1]

        if nums[rp] < nums[rp - 1]:
            return nums[rp]

        lp += 1
        rp -= 1

    return nums[0]


if __name__ == '__main__':
    nums = [2]
    print(run(nums))

    nums = [2, 1]
    print(run(nums))

    nums = [3, 4, 5, 6, 1]
    print(run(nums))

    nums = [3, 4, 5, 1, 2]
    print(run(nums))

    nums = [4, 5, 6, 7, 0, 1, 2]
    print(run(nums))

    nums = [19, 13, 15, 17]
    print(run(nums))

    nums = [11, 13, 15, 17]
    print(run(nums))
