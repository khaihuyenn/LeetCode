class Solution(object):
    def groupAnagrams(self, strs):
        result = defaultdict(list)
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] += 1
            result[tuple(counter)].append(s)
        return result.values()
        