class Solution(object):
    def findDuplicates(self, nums):
        duplicates = set()
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                duplicates.add(abs(num))
            else:
                nums[index] = -nums[index]
        return duplicates
        