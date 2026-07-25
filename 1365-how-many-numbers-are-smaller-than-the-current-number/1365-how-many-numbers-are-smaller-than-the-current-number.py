class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        tmp = sorted(nums)
        dic = {}
        ret = []
        for ind,val in enumerate(tmp):
            if val not in dic:
                dic[val] = ind
        for i in range(len(nums)):
            ret.append(dic[nums[i]])
        return ret
        