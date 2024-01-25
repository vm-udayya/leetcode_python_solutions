# Solution 1 
class Solution:
    def minRemoveToMakeValid(
        self, s: str, res: str = "", l: str = "(", r: str = ")", b: int = 0
    ) -> str:
        for _ in range(2):
            for c in s:
                if c == r and b <= 0:
                    continue
                b += c == l
                b -= c == r
                res += c
            res, s, l, r, b = "", res[::-1], r, l, 0
        return s
#Solution 2
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
            
        for i in stack:
            s[i] = ''

        return ''.join(s)
