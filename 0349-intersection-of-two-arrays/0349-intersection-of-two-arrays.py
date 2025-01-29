class Solution(object):
    def intersection(self, nums1, nums2):
        seen = {}
        result = []
        for num in nums1:
            seen[num] = 1
        for num in nums2:
            if num in seen and seen[num] == 1:
                result.append(num)
                seen[num] = 0
        return result
        