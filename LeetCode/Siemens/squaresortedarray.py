def make_squares(arr):
    lp = 0
    rp = len(arr) - 1
    squared = [-1 for _ in range(len(arr))]

    dec_counter = len(arr) - 1
    while lp <= rp:
        if abs(arr[lp]) >= abs(arr[rp]):
            squared[dec_counter] = arr[lp] * arr[lp]
            lp += 1
        else:
            squared[dec_counter] = arr[rp] * arr[rp]
            rp -= 1
        dec_counter -= 1

    return squared


def main():
    print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
    print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


if __name__ == '__main__':
    main()
