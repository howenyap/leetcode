class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        res = list()
        i = 0 

        while i < n1 and i < n2:
            res.append(word1[i])
            res.append(word2[i])
            i += 1 
        
        if i < n1:
            res.extend(word1[i:])
        elif i < n2: 
            res.extend(word2[i:])

        return "".join(res)
        
