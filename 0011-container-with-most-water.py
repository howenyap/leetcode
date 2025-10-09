from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        l, r = 0, n - 1

        while l < r:
            curr = min(height[l], height[r]) * (r - l)
            res = max(res, curr)

            if height[l] > height[r]:        
                r -= 1
            else:
                l += 1

        return res
