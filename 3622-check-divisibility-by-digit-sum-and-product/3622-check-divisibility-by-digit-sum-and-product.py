class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num = n
        s = 0
        p = 1
        while num>0:
            s += num%10
            p *= num%10
            num = num//10
        s1 = s+p
        return n%s1==0
        