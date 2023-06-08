# https://leetcode.com/problems/two-sum/
def run(nums, target):
    arr_size = len(nums)
    start = 0
    while start < arr_size - 1:
        end = start + 1
        while end < arr_size:
            # print(nums[start:end + 1])
            if nums[start] + nums[end] == target:
                return [start, end]
            end += 1
        start += 1


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
