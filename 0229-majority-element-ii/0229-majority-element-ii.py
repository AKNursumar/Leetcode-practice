class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        arr = []
        for num,count in counts.items():
            if count>len(nums)//3:
                arr.append(num)
        return arr

                


        