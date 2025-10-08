from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return max(nums)

        prev1 = max(nums[:2])
        prev2 = nums[0]

        for i in range(2, n):
            rob = nums[i] + prev2
            skip = prev1 

            prev2, prev1 = prev1, max(rob, skip)

        return prev1
        
