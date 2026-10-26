class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        small = []
        equal = []
        large = []
        for i in range(len(nums)):
            if nums[i]==pivot:
                equal.append(nums[i])
            elif nums[i]<pivot:
                small.append(nums[i])
            else:
                large.append(nums[i])
        return small+equal+large
        
        