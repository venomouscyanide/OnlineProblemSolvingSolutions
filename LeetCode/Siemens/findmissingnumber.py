def find_missing_number(nums):
    n = len(nums)
    i = 0

    while i < len(nums):

        if nums[i] != i:
            if nums[i] < len(nums):
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            else:
                i += 1
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i:
            return i

    return n


def main():
    print(find_missing_number([4, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


if __name__ == '__main__':
    main()
