from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = zeroes = l = 0

        for r in range(n):
            if nums[r] == 0:
                zeroes += 1

            while zeroes > 1:
                zeroes -= nums[l] == 0
                l += 1

            res = max(res, r - l)

        return res

