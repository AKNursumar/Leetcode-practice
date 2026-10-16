class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        n = len(nums)
        for i in range(n//2):
            res.append(nums[i])
            res.append(nums[i+n//2])
        return res