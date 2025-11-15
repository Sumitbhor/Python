def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            print(arr)
        arr[j + 1] = key
        print(arr)
        print()
arr = [25, 13, 4, 1, 22,78,9]
insertion_sort(arr)
print("Sorted array:", arr)
