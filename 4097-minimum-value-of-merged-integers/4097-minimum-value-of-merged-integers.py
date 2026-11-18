class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        m = float('inf')
        for i in range(0,len(nums),2):
            m = min(m,int(str(nums[i])+str(nums[i+1])))
        return m
        