class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        m = max(nums)
        n = min(nums)
        arr = []
        for i in range(n,m):
            if i not in nums:
                arr.append(i)
        return arr


        