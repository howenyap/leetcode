from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()

        def dfs(city: int) -> None:
            seen.add(city)

            for neighbour, connected in enumerate(isConnected[city]):
                if connected and neighbour not in seen:
                    dfs(neighbour)
        
        province = 0

        for city in range(len(isConnected)):
            if city not in seen:
                province += 1 
                dfs(city)
        
        return province

