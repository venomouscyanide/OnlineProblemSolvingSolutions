def selection_sort(arr):
    for i in range(len(arr)):
        j = i + 1
        largest = i
        while j < len(arr):
            if arr[j] > arr[i]:
                largest = j
            j += 1
        arr[i], arr[largest] = arr[largest], arr[i]


if __name__ == '__main__':
    arr = [1, 5, 2, 4, 1, 22]
    selection_sort(arr)
    print(arr)
