class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if nums[i]%2==0:
                ans.append(0)
            else:
                ans.append(1)
        ans.sort()
        return ans
        