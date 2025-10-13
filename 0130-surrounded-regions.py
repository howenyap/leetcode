from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ROWS, COLS = len(board), len(board[0])
        safe = set()

        def dfs(r: int, c: int):
            if board[r][c] != "O" or (r, c) in safe:
                return

            pos = (r, c)
            safe.add(pos)

            for dr, dc in DIRECTIONS:
                row = r + dr
                col = c + dc

                if 0 <= row < ROWS and 0 <= col < COLS:
                    dfs(row, col)

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)

        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in safe:
                    board[r][c] = "X"

