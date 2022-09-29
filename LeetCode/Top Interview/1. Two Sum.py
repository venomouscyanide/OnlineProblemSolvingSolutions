# https://leetcode.com/problems/two-sum/
def run(nums, target):
    # actual check
    for outer_index, candidate in enumerate(nums):
        # 2, 7
        rest = nums[outer_index + 1:]
        for inner_index, inner_can in enumerate(nums[outer_index + 1:]):
            if inner_can + candidate == target:
                return outer_index, inner_index + outer_index + 1


if __name__ == '__main__':
    nums = [-1, -2, -3, -4, -5]
    target = -8
    print(run(nums, target))

    nums = [3, 2, 4]
    target = 6
    print(run(nums, target))

    nums = [3, 3]
    target = 6
    print(run(nums, target))

    nums = [0, 4, 3, 0]
    target = 0
    print(run(nums, target))

    nums = [-1, -2, 10, 20]
    target = 8
    print(run(nums, target))
