class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            sum = 0
            n = num
            while n>0:
                sum +=n%10
                n = n//10
            num = sum
            if len(str(num)) == 1:
                return num
        