from typing import List
from math import inf

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n1 = n2 = inf

        for num in nums:
            if num < n1: 
                n1 = num
            elif n1 < num < n2:
                n2 = num
            elif num > n2:
                return True 
        
        return False 
        
