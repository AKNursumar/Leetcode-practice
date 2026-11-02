class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        med = nums[len(nums)//2]
        c = 0
        for num in nums:
            c += abs(med - num)
        return c