def selection_sort(arr):
    for i in range(len(arr) - 1):
        largest = i

        for j in range(i + 1, len(arr)):
            if arr[largest] <= arr[j]:
                largest = j

        arr[largest], arr[i] = arr[i], arr[largest]


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j >= 1:
            if arr[j] >= arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


def binary_search(arr, target):
    lp = 0
    rp = len(arr) - 1
    while lp <= rp:
        mid = (lp + rp) // 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            lp = lp + 1
        else:
            rp = rp - 1
    return -1


def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fib_driver(n):
    output_seq = []
    for i in range(n):
        output_seq.append(fibonacci(i))

    return output_seq


if __name__ == '__main__':
    print(fib_driver(10))

    arr = [1, 2, 3, 4, 5, 11, 2, 0, 22, 101, -1]
    arr_copy = arr.copy()
    selection_sort(arr_copy)
    print(arr_copy)

    arr_copy = arr.copy()
    bubble_sort(arr_copy)
    print(arr_copy)

    arr_copy = arr.copy()
    insertion_sort(arr_copy)
    print(arr_copy)

    arr.sort()
    print(arr)
    print(binary_search(arr, -1))

    arr_copy = arr.copy()
    merge_sort(arr_copy)
    print(arr_copy)
