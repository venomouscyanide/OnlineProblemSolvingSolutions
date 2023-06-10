def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j >= 1 and arr[j] >= arr[j - 1]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1


if __name__ == '__main__':
    arr = [1, 2, 33, 3, 4, 5]
    insertion_sort(arr)
    print(arr)
