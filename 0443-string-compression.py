from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        l = write = 0

        while l < n:
            r = l

            while r < n and chars[r] == chars[l]:
                r += 1 
            
            chars[write] = chars[l]
            write += 1

            count = r - l
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

            l = r
        
        return write 
