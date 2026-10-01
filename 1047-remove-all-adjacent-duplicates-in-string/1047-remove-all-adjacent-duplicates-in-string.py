class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        s1 = ""
        for ch in s:
            if stack and stack[-1]==ch:
                stack.pop()
            else:
                stack.append(ch)
        for ch in stack:
            s1 += ch
        return s1

        