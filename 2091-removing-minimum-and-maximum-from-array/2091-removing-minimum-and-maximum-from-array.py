class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        ind1 = nums.index(max(nums))
        ind2 = nums.index(min(nums))
        left_r = max(ind1,ind2) + 1
        right_r = len(nums) - min(ind1,ind2)
        bet_r = min(ind1,ind2)+1 + len(nums) - max(ind1,ind2)
        return min(left_r,right_r,bet_r)
        