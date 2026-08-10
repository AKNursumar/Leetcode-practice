class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = deque()
        l = 0
        r = len(nums)-1
        while l<=r:
            if abs(nums[l])<=abs(nums[r]):
                res.appendleft(nums[r]*nums[r])
                r-=1
            else:
                res.appendleft(nums[l]*nums[l])
                l+=1
        return list(res)
        