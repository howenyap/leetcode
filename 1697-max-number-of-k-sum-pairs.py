from typing import List
from collections import Counter

class Solution:
    # tc: n log n
    # sc: 1
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l, r = 0, n - 1 
        res = 0

        while l < r:
            curr = nums[l] + nums[r]
            if curr == k:
                res += 1
                l += 1
                r -= 1
            elif curr < k:
                l += 1
            else:
                r -= 1

        return res
        

    # tc: n
    # sc: n
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        res = 0

        for number, count in counter.items():
            diff = k - number

            if diff not in counter:
                continue

            pairs = count // 2 if number == diff else min(count, counter[diff])
            res += pairs
            counter[number] -= pairs
            counter[diff] -= pairs

        return res

