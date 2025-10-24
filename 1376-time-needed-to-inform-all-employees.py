from typing import List
from collections import deque, defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        d = defaultdict(list) 

        for i, m in enumerate(manager):
            d[m].append(i)

        q = deque([(headID, 0)])
        res = 0

        while q:
            u, t = q.popleft()
            res = max(res, t)

            for employee in d[u]:
                q.append((employee, t + informTime[u]))
        
        return res

