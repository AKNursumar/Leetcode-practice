class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        tmp = sorted(set(nums),reverse = True)
        if len(tmp)<3:
            return tmp[0]
        return tmp[2]


        
        