class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)//2
        counts = Counter(nums)
        for num,count in counts.items():
            if count == n:
                return num
        