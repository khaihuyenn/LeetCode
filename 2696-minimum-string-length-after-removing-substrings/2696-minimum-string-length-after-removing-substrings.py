class Solution(object):
    def minLength(self, s):
        # Initialize an empty stack
        stack = []
        # Iterate over each character
        for c in s:
            if stack and c == 'B' and stack[-1] == 'A':
                stack.pop()
            elif stack and c == 'D' and stack[-1] == 'C':
                stack.pop()
            else:
                stack.append(c)
        return len(stack)
        