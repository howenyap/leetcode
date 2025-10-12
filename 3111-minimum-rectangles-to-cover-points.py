from typing import List

class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        x_coordinates = sorted(set(x for x, _ in points))
        n = len(x_coordinates)
        res = i = 0
        
        while i < n:
            res += 1
            j = i

            while j < n and x_coordinates[j] <= x_coordinates[i] + w:
                j += 1

            i = j

        return res
 
