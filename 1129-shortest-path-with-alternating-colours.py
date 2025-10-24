from typing import List
from collections import defaultdict, deque 

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red, blue = 0, 1
        adj = [defaultdict(list), defaultdict(list)]

        for u, v in redEdges:
            adj[red][u].append(v)

        for u, v in blueEdges:
            adj[blue][u].append(v)

        res = [-1] * n
        q = deque([(0, 0, red), (0, 0, blue)])
        seen = set([(0, red), (0, blue)])

        while q:
            u, dist, prev = q.popleft()
            nxt = red if prev == blue else blue 

            if res[u] == -1:
                res[u] = dist

            for v in adj[nxt][u]:
                key = (v, nxt)

                if key not in seen: 
                    seen.add(key)
                    q.append((v, dist + 1, nxt))
        
        return res


