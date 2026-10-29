class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr = 0
        for i in range(k):
            curr += nums[i]
        m = curr
        for i in range(1,len(nums)-k+1):
            curr = curr - nums[i-1] + nums[i+k-1]
            m = max(m,curr)
        return m/k