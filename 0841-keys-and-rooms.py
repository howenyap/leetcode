from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set()

        def dfs(key: int) -> None: 
            seen.add(key)

            for room in rooms[key]: 
                if room not in seen:
                    dfs(room)
        
        dfs(0)
        
        return len(seen) == len(rooms)
        
