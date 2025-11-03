class Solution(object):
    def groupAnagrams(self, strs):
        map = {}
        for word in strs:
            counter = [0] * 26
            for char in word:
                counter[ord(char) - ord('a')] += 1
            key = ''.join(str(counter))
            if key not in map:
                map[key] = []
            map[key].append(word)
        return list(map.values())