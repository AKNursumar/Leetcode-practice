class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        if len(candyType)/2>len(set(candyType)):
            return len(set(candyType))
        return len(candyType)//2

        