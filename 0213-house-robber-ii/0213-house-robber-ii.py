class Solution:
    def solve(self,nums):
        n = len(nums)
        dp = [0]*(n)
        dp[0] = nums[0]
        for i in range(1,n):
            if n>1:
                pick = nums[i]+dp[i-2]
                not_pick = dp[i-1]
            else:
                pick = nums[i]
                not_pick = dp[i-1]
            dp[i] = max(pick,not_pick)
        return dp[n-1]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        return max(self.solve(nums[1:n]),self.solve(nums[0:n-1]))

        