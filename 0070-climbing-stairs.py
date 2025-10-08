class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev1 = 2
        prev2 = 1

        for _ in range(2, n):
            prev1, prev2 = prev2 + prev1, prev1

        return prev1 
        
