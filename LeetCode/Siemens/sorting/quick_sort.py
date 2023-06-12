LeetCode/Siemens/sorting/quick_sort.py# currently descending order
def quick_sort_helper(arr, first, last):
    if first < last:
        pivot_index = quick_sort(arr, first, last)
        quick_sort_helper(arr, pivot_index + 1, last)
        quick_sort_helper(arr, first, pivot_index - 1)


def quick_sort(arr, first, last):
    pivot = arr[first]

    lp = first + 1
    rp = last

    sentinel = True
    while sentinel:

        while lp <= rp and arr[lp] >= pivot:
            lp += 1

        while lp <= rp and arr[rp] <= pivot:
            rp -= 1

        if lp < rp:
            arr[lp], arr[rp] = arr[rp], arr[lp]
        else:
            sentinel = False

    arr[first], arr[rp] = arr[rp], arr[first]
    return rp


if __name__ == '__main__':
    arr = [5, 1, 2, 4, 3]
    quick_sort_helper(arr, first=0, last=len(arr) - 1)
    print(arr)
