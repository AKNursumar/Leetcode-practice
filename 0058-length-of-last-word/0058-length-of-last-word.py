class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1 = s.strip()
        count = 0
        for ch in s1:
            count +=1
            if ch==" ":
                count = 0
        return count
        