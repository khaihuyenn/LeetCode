class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i==0 or flowerbed[i-1] == 0) and (i==len(flowerbed)-1 or flowerbed[i+1] == 0):
                n-=1
                flowerbed[i] = 1
        return False if n > 0 else True
        