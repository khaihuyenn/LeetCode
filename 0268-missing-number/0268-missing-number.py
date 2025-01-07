class Solution(object):
    def missingNumber(self, nums):
        total = 0
        for i in range(len(nums) + 1):
            total += i
        return total - sum(nums)
        