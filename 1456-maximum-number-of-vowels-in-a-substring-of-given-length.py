class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        chars = list(s)
        vowels = set('aeiou')
        res = window = sum(1 for c in chars[:k] if c in vowels)

        for i in range(k, n):
            window += 1 if chars[i] in vowels else 0
            window -= 1 if chars[i - k] in vowels else 0
            res = max(res, window)
        
        return res
        
