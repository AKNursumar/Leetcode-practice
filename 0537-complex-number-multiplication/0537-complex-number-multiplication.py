class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        r1 = ""
        r2 = ""
        i1 = ""
        i2 = ""

        for ch in num1:
            if ch == '+':
                break
            r1 +=ch
        if r1[0]=="-":
            r1 = -int(r1[1:])
        else:
            r1 = int(r1)

        for ch in num2:
            if ch == '+':
                break
            r2 +=ch
        if r2[0]=="-":
            r2 = -int(r2[1:])
        else:
            r2 = int(r2)

        for i in range(len(num1)-2,-1,-1):
            if num1[i]=='+':
                break
            i1 = num1[i]+i1
        if i1[0]=="-":
            i1 = -int(i1[1:])
        else:
            i1 = int(i1)

        for i in range(len(num2)-2,-1,-1):
            if num2[i]=='+':
                break
            i2 = num2[i]+i2
        if i2[0]=="-":
            i2 = -int(i2[1:])
        else:
            i2 = int(i2)

        return str(r1*r2-i1*i2)+"+"+str(r1*i2+r2*i1)+"i"

        