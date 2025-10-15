from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        good = n - 1

        for i in reversed(range(n - 1)):
            if i + nums[i] >= good:
                good = i
            
        return good == 0


