class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        first, last = strs[0], strs[-1]
        min_length = min(len(strs[0]), len(strs[-1]))
        i = 0
        while i < min_length and first[i] == last[i]:
            i += 1
        if i == 0:
            return ""
        return first[:i]
            

        