class Solution(object):
    def isPalindrome(self, s):
        new_s = '' # Initialize an empty new string
        for char in s:
            if char.isalnum():
                new_s += char.lower()
        return new_s == new_s[::-1]

        