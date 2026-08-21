class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        for i in range(len(s)):
            seen = set()
            count = 0
            for j in range(i,len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
                count+=1
                maxi = max(maxi,count)
        return maxi


        