class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<=1:
            return False
        stack = []
        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)
            else:
                if ch==')' and stack and stack[-1]=='(':
                    stack.pop()
                elif ch=='}' and stack and stack[-1]=='{':
                    stack.pop()
                elif ch==']' and stack and stack[-1]=='[':
                    stack.pop()
                else:
                    stack.append(ch)
        return not(stack)
                