class Solution:
    def reverseVowels(self, s: str) -> str:
        v = "aeiouAEIOU"
        l=0
        r=len(s)-1
        s = list(s)
        s1 = ""
        while l<r:
            if s[l] not in v:
                l+=1
            if s[r] not in v:
                r-=1
            if s[l] in v and s[r] in v:
                s[l],s[r] = s[r],s[l]
                r-=1
                l+=1
        for ch in s:
            s1 = s1 + ch
        return s1


        