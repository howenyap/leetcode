from collections import deque

class Solution:
    def reverseWords(self, s: str) -> str:
        res = deque()

        n = len(s)
        l = 0

        while l < n:
            if s[l] == " ": 
                l += 1
                continue

            r = l
            while r < n and s[r] != " ":
                r += 1
            res.appendleft(s[l:r])
            l = r

        return " ".join(res)
