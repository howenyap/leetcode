from typing import List

# binary search
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in reversed(range(n - 1)):
            dp[i] = 1 + dp[i + 1] if nums[i] < nums[i + 1] else 1
        
        l, r = 1, n // 2

        while l <= r:
            k = (l + r) // 2
            found = False

            for i in range(n - 2 * k + 1):
                if dp[i] >= k and dp[i + k] >= k:
                    found = True
                    break

            if found: 
                l = k + 1
            else:
                r = k - 1
        
        return r

# linear
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        start = [1] * n
        end = [1] * n

        for i in reversed(range(n - 1)):
            if nums[i] < nums[i + 1]:
                start[i] = start[i + 1] + 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                end[i] = end[i - 1] + 1

        return max(min(end[i], start[i + 1]) for i in range(n - 1))

        
