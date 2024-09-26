class Solution(object):
    def findDuplicates(self, nums):
        count_dict = {}
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        duplicates = []
        for num, count in count_dict.items():
            if count > 1:
                duplicates.append(num)
        return duplicates
        
        