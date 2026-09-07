class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftsum = [0]*n
        rightsum = [0]*n
        ans = [0]*n
        s1 = s2 = sum(nums)
        for i in range(n-1,-1,-1):
            s1 = s1-nums[i]
            leftsum[i] = s1
        for i in range(n):
            s2 = s2 - nums[i]
            rightsum[i] = s2
            ans[i] = abs(leftsum[i]-rightsum[i])
        return ans
        