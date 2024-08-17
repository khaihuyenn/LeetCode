class Solution(object):
    def isPalindrome(self, s):
        new_s = ''.join(char.lower() for char in s if char.isalnum())
        return new_s == new_s[::-1]

        