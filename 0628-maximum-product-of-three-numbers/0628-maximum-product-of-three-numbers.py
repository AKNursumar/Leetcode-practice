class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        l,r = 0,len(nums)-1
        ret = float('-inf')
        while l<r:
            if (nums[l]*nums[l+1]*nums[l+2])>(nums[r]*nums[r-1]*nums[r-2]):
                ret = max(ret,nums[l]*nums[l+1]*nums[l+2])
                l+=1
            ret = max(ret,nums[r]*nums[r-1]*nums[r-2])
            r-=1
        ret = max(ret,nums[0]*nums[1]*nums[len(nums)-1])
        return ret
        