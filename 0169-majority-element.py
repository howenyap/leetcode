from typing import List

# https://www.geeksforgeeks.org/theory-of-computation/boyer-moore-majority-voting-algorithm/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = count = 0

        for num in nums:
            if count == 0:
                target = num
                count = 1
            else:
                count += 1 if num == target else -1

        return target
        
