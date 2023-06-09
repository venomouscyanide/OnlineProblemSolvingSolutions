def remove_duplicates(arr):
    lp = 0
    rp = lp + 1

    new_arr = []
    while rp < len(arr):
        if arr[lp] == arr[rp]:
            rp += 1
        elif arr[lp] != arr[rp]:
            new_arr.append(arr[lp])
            lp = rp
            rp = lp + 1
    new_arr.append(arr[lp])

    return new_arr


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([12, 12]))


if __name__ == '__main__':
    main()
