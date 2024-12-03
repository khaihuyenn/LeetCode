class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # set() - Remove duplicates; list() - {} -> []
        new_nums = list(set(nums))   # O(n)
        new_nums.sort(reverse=True)  # O(nlogn)
        if len(new_nums) < 3: 
            return max(new_nums)
        else:
            return new_nums[2]