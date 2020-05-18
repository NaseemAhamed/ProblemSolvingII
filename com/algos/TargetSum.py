class Solution:
    def target_sum(self, list, target):
        dict = {}
        for i, num in enumerate(list):
            if target - num in dict:
                return [dict[target - num], i]
            dict[num] = i
        return "The sum pair does not exist"


print(Solution().target_sum([2, 4, 5], 8))
