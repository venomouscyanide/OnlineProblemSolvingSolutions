# https://leetcode.com/problems/maximum-product-subarray/
import copy


def run(nums):
    def __run(nums):
        tot = len(nums)

        for index in range(1, tot):
            if nums[index] != 0 and nums[index - 1] != 0:
                nums[index] = nums[index] * nums[index - 1]
        return max(nums)

    prd = max(__run(copy.deepcopy(nums)), __run(copy.deepcopy(nums[::-1])))
    return prd


if __name__ == '__main__':
    nums = [-3, 0, 1, -2]
    print(run(nums))

    nums = [-1, -2, -9, -6]
    print(run(nums))

    nums = [3, -1, 4]
    print(run(nums))

    nums = [-2, 3, -4]
    print(run(nums))

    nums = [2, 3, -2, 4]
    print(run(nums))

    nums = [-2, 0, -1]
    print(run(nums))

    nums = [0, 2]
    print(run(nums))
