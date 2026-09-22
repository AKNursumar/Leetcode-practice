class Solution:
    def isPalindromic(self, s: str) -> bool:
        s1 = ""
        for ch in s:
            a = bin(ord(ch))[2:]
            while len(a)<8:
                a = "0" + a
            s1 +=a
        if s1 == s1[::-1]:
            return True
        return False