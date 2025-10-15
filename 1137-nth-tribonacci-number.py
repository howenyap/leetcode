class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n <= 2:
            return 1
        
        prev3, prev2, prev1 = 0, 1, 1

        for _ in range(n - 2):
            prev3, prev2, prev1 = prev2, prev1, prev3 + prev2 + prev1 

        return prev1
        
