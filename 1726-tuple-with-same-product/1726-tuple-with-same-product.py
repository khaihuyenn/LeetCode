class Solution(object):
    def tupleSameProduct(self, nums):
        counter = {}
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]
                ans += 8 * counter.get(product, 0)
                counter[product] = counter.get(product, 0) + 1
        return ans
