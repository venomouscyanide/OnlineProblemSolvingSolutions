# https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/


def run(nums):
    minn = min(nums)
    minn_index = min([index for index, value in enumerate(nums) if value == minn])

    count = 0
    for index in range(minn_index, 0, -1):
        count += 1
        nums[index], nums[index - 1] = nums[index - 1], nums[index]

    maxx = max(nums)
    maxx_index = max([index for index, value in enumerate(nums) if value == maxx])
    count += len(nums) - maxx_index - 1

    return count


if __name__ == '__main__':
    nums = [3, 4, 5, 5, 3, 1]
    print(run(nums))

    nums = [1, 4, 5, 5, 3, 1]
    print(run(nums))

    nums = [1]
    print(run(nums))
