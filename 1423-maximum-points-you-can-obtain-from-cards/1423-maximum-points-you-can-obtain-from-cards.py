class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        arr = cardPoints + cardPoints
        right = sum(cardPoints[n-k:n])
        left = sum(cardPoints[:k])
        middle = sum(arr[n-k+1:n+1])
        curr = middle
        for i in range(n-k+2,n+1):
            curr += arr[i+k-1]
            curr -= arr[i-1]
            middle = max(middle,curr)
        return max(middle,right,left)
        
        