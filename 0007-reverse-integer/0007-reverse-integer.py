class Solution:
    def reverse(self, x: int) -> int:
        n=0
        if x<0:
            n =1
            x = -x
        total = 0
        
        while x>0:
            total = total*10 + x%10
            x = x//10
        if total<-2**31 or total>2**31-1:
            return 0
        if n==1:
            return -total
        return total
        
        