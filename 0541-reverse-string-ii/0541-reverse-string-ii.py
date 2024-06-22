class Solution(object):
    def reverseStr(self, s, k):
        # convert string into char array
        char = list(s)
        
        for i in range(0, len(s), 2*k):
            char[i:i+k] = reversed(char[i:i+k])
        return ''.join(char)
        
        