from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        dp = [1] * n
        res = -1

        for i in range(n):
            for j in range(i):
                curr = dp[j] + 1 if nums[j] < nums[i] else 1
                dp[i] = max(dp[i], curr)

            res = max(res, dp[i])
            
        return res
