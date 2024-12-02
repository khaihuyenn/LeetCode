class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        final_string = ""
        for char in s:
            if char != 'i':
                final_string += char
            else:
                final_string = final_string[::-1]
        return final_string

        #Time complexity: O(n^2)- in worst-case when every char is 'i' reversing happens O(n^2)
        #Space complexity: O(n)- the 'final_string' list 