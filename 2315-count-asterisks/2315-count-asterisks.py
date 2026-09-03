class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        pair = False
        for ch in s:
            if pair==False:
                if ch == "*":
                    count+=1
            if ch=="|":
                if pair==False:
                    pair = True
                else:
                    pair = False
        return count
            
        