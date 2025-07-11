class Solution(object):
    def productExceptSelf(self, nums):
        prod, zero_counter = 1, 0
        for num in nums:
            if num != 0:
                prod *= num
            else:
                zero_counter += 1
        if zero_counter > 1:
            return [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                if zero_counter == 1:
                    nums[i] = 0
                else:
                    nums[i] = prod // nums[i]
            else:
                nums[i] = prod
        return nums
        