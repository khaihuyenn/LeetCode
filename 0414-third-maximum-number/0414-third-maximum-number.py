class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, second, third = float('-inf'), float('-inf'), float('-inf')
        print(first, second, third)
        for num in nums:
            if num > first:
                first, second, third = num, first, second
            elif first > num > second:
                second, third = num, second
            elif second > num > third:
                third = num
        if third != float('-inf'):
            return third
        else:
            return first
        