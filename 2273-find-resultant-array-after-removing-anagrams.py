from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = list()
        prev = None

        for word in words:
            chars = [0] * 26

            for ch in word:
                chars[ord(ch) - 97] += 1

            if not prev or chars != prev:
                prev = chars
                res.append(word)

        return res
                
