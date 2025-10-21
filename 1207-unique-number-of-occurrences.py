from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        counts = counter.values()
        return len(counts) == len(set(counts)) 
        
