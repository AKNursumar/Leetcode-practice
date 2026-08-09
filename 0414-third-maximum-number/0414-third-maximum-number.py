class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m1=m2=m3 = float('-inf')
        for num in set(nums):
            if num>m1:
                m3 = m2
                m2 = m1
                m1 = num
            elif num>m2:
                m3 = m2
                m2 = num
            elif num>m3:
                m3 = num
        if m3!=float('-inf'):
            return m3
        return m1


        
        