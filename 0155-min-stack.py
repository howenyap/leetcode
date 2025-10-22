from math import inf

class MinStack:

    def __init__(self):
        self.stack = list()
        self.min = inf

    def push(self, val: int) -> None:
        self.stack.append((val, self.min))
        self.min = min(self.min, val)

    def pop(self) -> None:
        _, old_min = self.stack.pop() 
        self.min = old_min

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min
       
