class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = max(nums)
        c = 0
        for num in nums:
            c += m - num
        return c