class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev = nums[0]
        for i in range(1,len(nums)):
            pick = nums[i]+prev2
            not_pick = prev
            curr = max(pick,not_pick)
            prev2 = prev
            prev = curr
        return prev

        