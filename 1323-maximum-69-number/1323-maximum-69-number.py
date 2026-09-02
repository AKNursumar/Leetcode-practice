class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        s2 = ""
        ind = -5
        for i in range(len(s)):
            if s[i]=='6':
                ind = i
                break
        if ind == -5:
            return num
        for i in range(len(s)):
            if i == ind:
                s2 +="9"
            else:
                s2+=s[i]
        return int(s2)
        