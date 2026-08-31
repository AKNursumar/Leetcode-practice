class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        ind1 = nums.index(max(nums))
        ind2 = nums.index(min(nums))
        n = len(nums)
        r1 = max(ind1,ind2)
        r2 = min(ind1,ind2)
        left_r = r1 + 1
        right_r = n - r2
        bet_r = r2+1 + n - r1
        return min(left_r,right_r,bet_r)
        