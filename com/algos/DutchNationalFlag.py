# 2,1,3,1,2,3
def dutch_national_problem(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 1:
            nums[mid], nums[low] = nums[low], nums[mid]
            low += 1
            mid += 1
        elif nums[mid] == 2:
            mid += 1
        elif nums[mid] == 3:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums


print(dutch_national_problem([2, 1, 3, 1, 2, 2, 3, 1]))
