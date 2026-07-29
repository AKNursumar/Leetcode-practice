class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sum = 0
        s1 = ''
        while n>0:
            if n%10 != 0:
                s1 += str(n%10)
                sum +=n%10
            n = n//10
        if(len(s1)==0):
            return 0
        return sum*int(s1[::-1])
        

        