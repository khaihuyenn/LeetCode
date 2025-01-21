class Solution(object):
    def majorityElement(self, nums):
        majority = 0
        count = 0
        for i in range(len(nums)):
            if count == 0:
                majority = nums[i]
            count += 1 if nums[i] == majority else -1
        return majority
        