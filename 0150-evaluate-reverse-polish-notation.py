from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        ops = "+-*/"
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                right, left = stack.pop(), stack.pop()

                match token:
                    case "+":
                        res = left + right
                    case "-":
                        res = left - right
                    case "*":
                        res = left * right
                    case "/":
                        res = int(left / right) 
                stack.append(res)
        
        return stack[0] 
        
