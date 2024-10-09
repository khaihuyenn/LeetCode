class Solution(object):
    def isValid(self, s):
        brackets = {')':'(', '}':'{', ']':'['}
        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if stack and brackets[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
        