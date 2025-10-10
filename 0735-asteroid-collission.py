from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = list()

        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                prev = stack.pop()
                diff = prev + a

                if diff == 0:
                    break
                elif diff < 0:
                    continue
                else:
                    stack.append(prev)
                    break
            else:
                stack.append(a)
        
        return stack

