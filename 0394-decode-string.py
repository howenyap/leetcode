class Solution:
    def decodeString(self, s: str) -> str:
        stack = list()
    
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                chars = list() 
                while stack and stack[-1].isalpha():
                    chars.append(stack.pop())
                
                stack.pop()

                digits = list()
                while stack and stack[-1].isdigit():
                    digits.append(stack.pop())

                count = int("".join(map(str, reversed(digits)))) if digits else 1
                substring = "".join(reversed(chars))
                stack.append(count * substring)

        return "".join(stack)
        
