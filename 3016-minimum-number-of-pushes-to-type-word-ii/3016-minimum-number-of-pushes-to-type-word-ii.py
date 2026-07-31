class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word).most_common()
        arr = []
        count = 0
        for i in range(len(counts)):
            if i<8:
                count +=counts[i][1]
            if i>=8 and i<16:
                count +=counts[i][1]*2
            if i>=16 and i<24:
                count +=counts[i][1]*3
            if i>=24:
                count +=counts[i][1]*4
        return count
            
            
            



        