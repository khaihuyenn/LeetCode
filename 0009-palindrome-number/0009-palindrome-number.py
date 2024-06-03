class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_half = 0
        while x > reversed_half:
            reversed_half = (x % 10) + (reversed_half * 10)
            x = x // 10
        return x == reversed_half // 10 or x == reversed_half