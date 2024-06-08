class Solution(object):
    def trailingZeroes(self, n):
        trailing_zero = 0
        i = 5
        while n >= i: 
            trailing_zero += n // i
            i *= 5
        return trailing_zero   
        