# https://leetcode.com/problems/search-in-rotated-sorted-array/


def run(nums, target):
    lp = 0
    rp = len(nums) - 1

    idx = -1
    while lp < rp:
        if nums[lp] > nums[lp + 1]:
            idx = lp + 1

        if nums[rp] < nums[rp - 1]:
            idx = rp

        lp += 1
        rp -= 1

        if idx != -1:
            break

    if idx == -1:
        idx = 0

    if target >= nums[idx] and target <= nums[-1]:
        search_in = nums[idx:]
    else:
        search_in = nums[:idx]
        idx = 0

    # bin search
    lp = 0
    rp = len(search_in) - 1
    while lp <= rp:
        mid = (lp + rp) // 2

        if target > search_in[mid]:
            lp = mid + 1
        elif target < search_in[mid]:
            rp = mid - 1
        else:
            return mid + idx

    return -1


if __name__ == '__main__':
    nums = [1, 3, 5]
    target = 4
    print(run(nums, target))

    nums = [1, 3]
    target = 2
    print(run(nums, target))

    nums = [5, 6, 7, 8, 1, 2, 3, 4]
    target = 4
    print(run(nums, target))

    nums = [1]
    target = 1
    print(run(nums, target))

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(run(nums, target))

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    print(run(nums, target))

    nums = [1]
    target = 0
    print(run(nums, target))

    nums = [5, 6, 7, 8, 1, 2, 3, 4]
    target = 8
    print(run(nums, target))

    nums = [5, 6, 7, 8, 1, 2, 3, 4]
    target = 5
    print(run(nums, target))
