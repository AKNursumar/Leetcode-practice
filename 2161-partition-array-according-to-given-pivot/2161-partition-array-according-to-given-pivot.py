class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        small = []
        equal = []
        large = []
        for num in nums:
            if num==pivot:
                equal.append(num)
            elif num<pivot:
                small.append(num)
            else:
                large.append(num)
        return small+equal+large
        
        