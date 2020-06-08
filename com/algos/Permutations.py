class Solution:
    def permute(self, nums):
        res = []

        def permute_helper(start):
            if start == len(nums) - 1:
                return res.append(nums[:])
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                permute_helper(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        permute_helper(0)
        return res


print(Solution().permute([1, 2, 3]))
