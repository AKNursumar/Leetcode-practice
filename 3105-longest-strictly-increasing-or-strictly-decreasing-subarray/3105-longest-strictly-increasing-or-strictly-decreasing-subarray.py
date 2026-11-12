class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        c1 = 1
        c2 = 1
        n = len(nums)
        if n==1:
            return 1
        m1 = 0
        m2 = 0
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                c1+=1
            else:
                c1 = 1
            m1 = max(m1,c1)

        for i in range(1,n):
            if nums[i]<nums[i-1]:
                c2+=1
            else:
                c2 = 1
            m2 = max(m2,c2)

        return max(m1,m2)