class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        if n <=8:
            return n
        if n <=16 and n>8:
            return 8+2*(n-8)
        if n <=24 and n>16:
            return 24+3*(n-16)
        if n <=26 and n>24:
            return 48+4*(n-24)
        

        
        