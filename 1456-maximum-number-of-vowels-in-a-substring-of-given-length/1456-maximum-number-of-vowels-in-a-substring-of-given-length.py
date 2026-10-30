class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        c = 0
        n = len(s)
        vowels = 'aeiou'
        window = deque()
        for i in range(k):
            if s[i] in vowels:
                c +=1
            window.append(s[i])
        m = c
        for i in range(k,n):
            if s[i] in vowels:
                c+=1
            if window[0] in vowels:
                c-=1
            window.popleft()
            window.append(s[i])
            m = max(m,c)
        return m

        