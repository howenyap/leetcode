from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        if n > length: 
            return False

        spots = 0 

        for i in range(length):
            left = i == 0 or flowerbed[i-1] == 0
            right = i == length - 1 or flowerbed[i+1] == 0
            middle = flowerbed[i] == 0

            if left and middle and right: 
                flowerbed[i] = 1
                spots += 1

        return spots >= n
        
