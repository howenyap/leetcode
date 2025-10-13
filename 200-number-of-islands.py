from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> bool:
            if grid[r][c] == "0":
                return False

            grid[r][c] = "0"

            for dr, dc in DIRECTIONS: 
                row = r + dr
                col = c + dc

                if not (0 <= row < ROWS and 0 <= col < COLS):
                    continue
 
                if grid[row][col] != "1":
                    continue

                dfs(row, col)
            
            return True 
        
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c):
                    res += 1

        return res

        
