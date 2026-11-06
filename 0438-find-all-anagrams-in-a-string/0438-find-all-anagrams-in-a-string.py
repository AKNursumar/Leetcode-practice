class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n = len(s)
        w = len(p)
        if w>n:
            return []
        window = math.prod(ord(ch) for ch in p)
        curr = math.prod(ord(s[i]) for i in range(w))
        ans = []
        if curr == window:
            ans.append(0)
        for i in range(1,n-w+1):
            curr = curr// ord(s[i-1])
            curr *= ord(s[i+w-1])
            if curr == window:
                ans.append(i)
        return ans


        