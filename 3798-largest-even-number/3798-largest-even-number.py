class Solution:
    def largestEven(self, s: str) -> str:
        idx = -1
        for i in range(len(s)-1,-1,-1):
            if s[i] == "2":
                idx = i
                break
        if idx == -1:
            return ""
        else:
            return s[:idx+1]

        