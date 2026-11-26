class Solution:
    def canAliceWin(self, n: int) -> bool:
        b = 0
        i = 10
        while n>=0:
            if n-i>=0:
                n = n-i
            else:
                if b%2==0:
                    return False
                else:
                    return True
            i-=1
            b+=1
