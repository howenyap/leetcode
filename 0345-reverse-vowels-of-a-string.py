class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        l, r = 0, n - 1
        res = list(s)
        vowels = "aeiouAEIOU"

        while l < r:
            if res[l] not in vowels:
                l += 1

            if res[r] not in vowels:
                r -= 1
            
            if res[l] in vowels and res[r] in vowels:
                res[l], res[r] = res[r], res[l]
                l += 1
                r -= 1
        
        return "".join(res)
        
