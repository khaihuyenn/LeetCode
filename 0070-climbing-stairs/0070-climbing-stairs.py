class Solution(object):
    def climbStairs(self, n):
        # initialize the list with zeros, with an extra space for  the 0th step
        ways = [0] * (n + 1)
        ways[0], ways[1] = 1, 1
        for i in range(2, n + 1):
            ways[i] = ways[i - 2] + ways[i - 1]
        return ways[n]