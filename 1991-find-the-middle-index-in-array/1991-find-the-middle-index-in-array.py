class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        right = 0
        for i in range(len(nums)):
            if right == total-right-nums[i]:
                return i
            right += nums[i]
        return -1
        