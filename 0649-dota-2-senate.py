from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_count = senate.count("R")
        dire_count = len(senate) - radiant_count 
        radiant_votes = dire_votes = 0
        q = deque(senate) 

        while radiant_count and dire_count:
            curr = q.popleft()
            
            if curr == "R":
                if dire_votes:
                    radiant_count -= 1
                    dire_votes -= 1
                else:
                    radiant_votes += 1
                    q.append(curr)
            else:
                if radiant_votes:
                    dire_count -= 1
                    radiant_votes -= 1
                else:
                    dire_votes += 1
                    q.append(curr)

        return "Radiant" if radiant_count else "Dire"
        
