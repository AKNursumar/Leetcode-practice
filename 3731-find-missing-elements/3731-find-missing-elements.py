class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = []
        for num in range(nums[0],nums[-1]):
            if num not in nums:
                arr.append(num)
        return arr


        