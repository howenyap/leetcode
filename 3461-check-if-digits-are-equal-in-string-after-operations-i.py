class Solution:
    def hasSameDigits(self, s: str) -> bool:
        res = list(int(digit) for digit in s)

        while len(res) != 2:
            for i in range(len(res) - 1):
                res[i] = (res[i] + res[i + 1]) % 10

            res.pop()

        return res[0] == res[1]
        
