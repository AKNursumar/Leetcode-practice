class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        dic = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
        while n>0:
            dic[n%10] +=1
            n =n//10
        s = 0
        for n,m in dic.items():
            s +=n*m
        return s
        