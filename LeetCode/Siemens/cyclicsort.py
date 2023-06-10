def cyclic_sort(nums):
    # do not move on until the start is at the right index
    i = 0
    while i < len(nums):
        if nums[i] != i + 1:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        else:
            i += 1
    return nums


def main():
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))


if __name__ == '__main__':
    main()
