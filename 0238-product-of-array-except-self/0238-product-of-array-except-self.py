class Solution(object):
    def productExceptSelf(self, nums):
        zero_count = 0
        product = 1
        for num in nums:
            if num != 0:
                product *= num
            else:
                zero_count += 1
        answer = []
        if zero_count > 1:
            return [0] * len(nums)
        for num in nums:
            if num != 0:
                if zero_count == 1:
                    answer.append(0)
                else:
                    answer.append(product // num)
            else:
                answer.append(product)
        return answer
        