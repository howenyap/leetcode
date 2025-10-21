from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0

        for i, num in enumerate(nums):
            right = total - left - num

            if left == right:
                return i

            left += num
        
        return -1
        
