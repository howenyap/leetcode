from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True

        n = len(nums)
        dp = [1] * n

        for i in reversed(range(n - 1)):
            dp[i] = dp[i + 1] + 1 if nums[i + 1] > nums[i] else 1

        for i in range(n - 2 * k + 1):
            if dp[i] >= k and dp[i + k] >= k:
                return True
                
        return False

        
