# currently descending order
def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left_sub = arr[:middle]
        right_sub = arr[middle:]

        merge_sort(left_sub)
        merge_sort(right_sub)

        i = j = k = 0

        while i < len(left_sub) and j < len(right_sub):
            if left_sub[i] >= right_sub[j]:
                arr[k] = left_sub[i]
                i += 1
            else:
                arr[k] = right_sub[j]
                j += 1
            k += 1

        while i < len(left_sub):
            arr[k] = left_sub[i]
            k += 1
            i += 1

        while j < len(right_sub):
            arr[k] = right_sub[j]
            k += 1
            j += 1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    merge_sort(arr)
    print(arr)
