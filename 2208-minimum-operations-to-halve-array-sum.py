from typing import List
from collections import heapq

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        heap = [-n for n in nums]
        heapq.heapify(heap)

        curr = sum(nums)
        target = curr / 2
        res = 0

        while curr > target:
            x = -heapq.heappop(heap)
            half = x / 2
            curr -= half
            heapq.heappush(heap, -half)
            res += 1

        return res
        
