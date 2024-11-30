class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniques = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[uniques]:
                uniques += 1
                nums[uniques] = nums[i]
        return uniques + 1
        