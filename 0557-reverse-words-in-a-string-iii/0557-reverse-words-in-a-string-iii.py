class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reverse = ""
        for word in words:
            reverse += word[::-1] + " "
        return reverse.strip()
        