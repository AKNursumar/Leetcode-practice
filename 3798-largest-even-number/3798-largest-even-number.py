class Solution:
    def largestEven(self, s: str) -> str:
        s= int(s)
        while s%2!=0:
            s= s//10
        if s>0:
            return str(s)
        return ""


        