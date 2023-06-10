def bin_search(arr, target):
    lp = 0
    rp = len(arr)

    while lp <= rp:
        middle = (lp + rp) // 2

        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            rp = middle - 1
        else:
            lp = middle + 1
    return -1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    target = -13
    print(bin_search(arr, target))
