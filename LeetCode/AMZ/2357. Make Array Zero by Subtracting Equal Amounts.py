def run(nums):
    iter = 0
    while max(nums) != 0:
        iter += 1
        min_non_zero = min(filter(lambda x: x > 0, nums))
        nums = [x - min_non_zero if x > 0 else x for x in nums]
    return iter


if __name__ == '__main__':
    nums = [1, 5, 0, 3, 5]
    print(run(nums))

    nums = [0]
    print(run(nums))
