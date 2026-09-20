class Solution:
    def reverseDegree(self, s: str) -> int:
        s1 = "0zyxwvutsrqponmlkjihgfedcba"
        su = 0
        for i in range(len(s)):
            su += s1.index(s[i])*(i+1)
        return su