class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = list()
        segments = list(filter(bool, path.split("/"))) 

        for segment in segments: 
            if segment == '.':
                continue
            elif segment == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(segment)
            
        return "/" + "/".join(stack)
        
