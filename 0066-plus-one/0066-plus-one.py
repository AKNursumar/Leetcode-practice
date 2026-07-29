class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s1 = ""
        ret = []
        for num in digits:
            s1 += str(num)
        num = int(s1)+1
        s1 = str(num)
        for ch in s1:
            ret.append(int(ch))
        return ret

        