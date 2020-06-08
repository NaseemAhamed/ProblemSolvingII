class Solution:
    def find_first_n_last_index(self, arr, target):
        first = self.binary_search(arr, 0, len(arr) - 1, target, True)
        last = self.binary_search(arr, 0, len(arr) - 1, target, False)
        return [first, last]

    def binary_search(self, arr, lower, upper, target, find_first):
        while True:
            if upper < lower:
                return -1
            mid = lower + (upper - lower) // 2  # 13334
            if find_first:
                if (mid == 0 or arr[mid - 1] < target) and arr[mid] == target:
                    return mid
                elif target > arr[mid]:
                    lower = mid + 1
                else:
                    upper = mid - 1
            else:
                if (mid == len(arr) - 1 or target < arr[mid + 1]) and arr[mid == target]:
                    return mid
                elif target < arr[mid]:
                    upper = mid - 1
                else:
                    lower = mid + 1


arr = [1, 3, 3, 3, 3, 4]
print(Solution().find_first_n_last_index(arr, 3))
