class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:   # Edge case: empty array
            return 0

        if len(nums) == 1:
            return 1

        uniques = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[uniques]:
                uniques += 1
                if uniques != i:
                    nums[uniques] = nums[i]
        return uniques + 1
        