class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        counterS, counterT = {}, {}
        for i in range(len(s)):
            counterS[s[i]] = counterS.get(s[i], 0) + 1
            counterT[t[i]] = counterT.get(t[i], 0) + 1
        return counterS == counterT
        