class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sum = 0
        s1 = str(n)
        s2 = ""
        for ch in s1:
            if int(ch)!=0:
                s2 +=ch
                sum +=int(ch)
        if len(s2)==0:
            return 0
        return sum*int(s2)
        

        