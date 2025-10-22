class Solution:
    def calculate(self, s: str) -> int:
        res = curr = 0
        sign = 1
        stack = list()

        for c in s:
            if c.isdigit():
                curr = 10 * curr + int(c)
            elif c == ")":
                res += curr * sign
                curr = 0

                prev_sign, prev_res = stack.pop(), stack.pop()
                res *= prev_sign
                res += prev_res
            elif c == "(":
                stack.append(res)
                stack.append(sign)

                res = 0
                curr = 0
                sign = 1
            elif c in "+-":
                res += sign * curr
                curr = 0
                sign = 1 if c == "+" else -1

        return res + curr * sign

