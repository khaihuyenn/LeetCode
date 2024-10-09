class Solution(object):
    def minAddToMakeValid(self, s):
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            elif stack[-1] == '(' and c == ')':
                stack.pop()
            else:
                stack.append(c)
        return len(stack)
        