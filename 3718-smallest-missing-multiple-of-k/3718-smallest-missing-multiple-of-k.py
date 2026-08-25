class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n =0
        for i in range(1,len(nums)+1):
            if i*k not in nums:
                return i*k
            n = i
        return (n+1)*k
        