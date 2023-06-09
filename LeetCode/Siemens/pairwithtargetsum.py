def pair_with_targetsum(arr, target_sum):
    lp = 0
    rp = len(arr) - 1
    while lp < rp:
        curr_sum = arr[lp] + arr[rp]
        if curr_sum == target_sum:
            return lp, rp
        elif curr_sum > target_sum:
            rp = rp - 1
        else:
            lp = lp + 1
    return lp, rp


def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))


if __name__ == '__main__':
    main()
