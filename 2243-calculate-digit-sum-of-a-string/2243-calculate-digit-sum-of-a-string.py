class Solution:
    def digitSum(self, s: str, k: int) -> str:
        s2=""
        sm = 0
        if len(s)<=k:
            return s
        while True:
            for i in range(len(s)):
                sm +=int(s[i])
                if i>0 and (i+1)%k==0:
                    s2+=str(sm)
                    sm =0
            if len(s)%k!=0:
                s2 +=str(sm)
                sm = 0
            if len(s2)<=k:
                return s2
            s = s2
            s2 = ""
                
