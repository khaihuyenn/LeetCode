class Solution(object):
    def thirdMax(self, nums):
        first, second, third = float('-inf'), float('-inf'), float('-inf')
        #Base case:
        if len(nums) < 3:
            return max(nums)

        for num in nums:
            if num > first:
                third = second
                second = first
                first  = num
            elif second < num < first:
                third = second
                second = num
            elif third < num < second:
                third = num
        return third if third != float('-inf') else first
        