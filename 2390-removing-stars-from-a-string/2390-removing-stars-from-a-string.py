class Solution:
    def removeStars(self, s: str) -> str:
        s1 = []
        for ch in s:
            if ch == '*':
                s1.pop()
            else:
                s1.append(ch)
        return "".join(s1)
        