class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        count = 0
        n = len(nums)//3
        arr = []
        for i in range(len(nums)):
            if i+1<len(nums):
                if nums[i]==nums[i+1]:
                    count +=1
                else:
                    count =0
            if count>=n and nums[i] not in arr:
                arr.append(nums[i])
        return arr
                


        