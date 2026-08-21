class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumodd=0
        sumeven=0
        for i in range(1,2*n+1):
            if i%2!=0:
                sumodd +=i
            else:
                sumeven += i
        while sumeven!=0:
            tmp = sumeven
            sumeven = sumodd%sumeven
            sumodd = tmp
        return sumodd
        