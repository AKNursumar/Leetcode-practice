class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        s1 = ""
        res = ""
        dic = dict(knowledge)
        i = 0
        while i<len(s):
            if s[i] == '(':
                i+=1
                while s[i]!=')':
                    s1 += s[i]
                    i+=1
                if s1 in dic:
                    res += dic[s1]
                else:
                    res +='?'
                s1 = ""
            else:
                res += s[i]
            i+=1
        return res 

        