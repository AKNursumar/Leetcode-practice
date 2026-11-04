class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = 1
        n = len(s1)
        m = len(s2)
        s2_ascii = []

        for i in range(n):
            c1 *= ord(s1[i])

        for i in range(m):
            s2_ascii.append(ord(s2[i]))

        c2 =  math.prod(s2_ascii[:n])
        if c1 == c2:
            return True
        for i in range(1,m-n+1):
            c2 = c2//s2_ascii[i-1]
            c2 *= s2_ascii[i+n-1]
            if c1 == c2:
                return True
        return False

        