def binary_search(arr, lower, upper, x):
    while lower <= upper:
        mid = lower + (upper - lower) // 2
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            lower = mid + 1
        else:
            upper = mid - 1
    return -1


arr = [1, 2, 5, 7, 9]
num_to_search = 5
result = binary_search(arr, 0, len(arr) - 1, num_to_search)
if result != -1:
    print("The element is available at the index ", result)
else:
    print("The element is not available")
