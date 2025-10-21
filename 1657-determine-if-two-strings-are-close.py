from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)

        if counter1 == counter2:
            return True
        
        sameCharacterSet = counter1.keys() == counter2.keys()
        sameFrequencySet = Counter(counter1.values()) == Counter(counter2.values())

        return sameCharacterSet and sameFrequencySet
        
