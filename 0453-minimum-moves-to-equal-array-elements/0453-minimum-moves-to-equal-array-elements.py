class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mn = min(nums)
        s = 0
        for num in nums:
            s += num - mn
        return s