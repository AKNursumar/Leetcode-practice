class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        res = []
        for num,count in counts.items():
            if count==2:
                res.append(num)
        return res
        