from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        if n <= 2:
            return min(cost)

        next1, next2 = cost[-2], cost[-1]

        for i in reversed(range(n - 2)):
            next1, next2 = cost[i] + min(next1, next2), next1

        return min(next1, next2) 

