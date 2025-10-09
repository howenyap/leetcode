from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = zeroes = l = 0

        for r in range(n):
            if nums[r] == 0:
                zeroes += 1 

            while zeroes > k:
                zeroes -= nums[l] == 0
                l += 1

            res = max(res, r - l + 1)

        return res

