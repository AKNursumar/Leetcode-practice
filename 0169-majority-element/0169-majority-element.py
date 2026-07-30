class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        counts = Counter(nums)
        for num in nums:
            if counts[num] >= n/2:
                return num
        