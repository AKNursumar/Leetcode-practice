class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for ch in operations:
            if ch not in "CD+":
                stack.append(int(ch))
            if ch == 'C':
                stack.pop()
            if ch == 'D':
                stack.append(stack[-1]*2)
            if ch == '+':
                stack.append(stack[-1]+stack[-2])
        return sum(stack)
        