from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = window = sum(nums[:k])
        n = len(nums)

        for i in range(k, n): 
            window += nums[i] - nums[i-k]
            res = max(res, window)

        return res / k
        
