class MyQueue:

    def __init__(self):
        self.input = list()
        self.output = list()

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.transfer()
        return self.output.pop()

    def peek(self) -> int:
        self.transfer()
        return self.output[-1]

    def empty(self) -> bool:
        return len(self.input) == 0 and len(self.output) == 0
    
    def transfer(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

