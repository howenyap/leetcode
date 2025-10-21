from typing import List
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        grid_t = zip(*grid)
        cols = Counter(grid_t)

        return sum(cols[tuple(row)] for row in grid) 
        

