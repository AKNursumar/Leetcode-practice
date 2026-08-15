class Solution:
    def removeStars(self, s: str) -> str:
        s1 = ""
        for ch in s:
            if ch == '*':
                s1 = s1[0:-1]
            else:
                s1 = s1 + ch
        return s1
        