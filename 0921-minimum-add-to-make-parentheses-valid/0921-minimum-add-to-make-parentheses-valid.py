class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        total = 0
        for ch in s:
            if ch == ')':
                if stack and stack[-1]=='(':
                    stack.pop()
                    total -=1
                else:
                    stack.append(ch)
                    total += 1
            else:
                stack.append(ch)
                total +=1
        return total
        