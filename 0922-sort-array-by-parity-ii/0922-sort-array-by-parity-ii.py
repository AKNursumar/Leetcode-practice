class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        ans = []
        odd = []
        even = []
        n = len(nums)
        for i in range(n):
            if nums[i] %2 !=0:
                odd.append(nums[i])
            else:
                even.append(nums[i])

        for i in range(n):
            if i %2 !=0:
                ans.append(odd[0])
                odd.remove(odd[0])
            else:
                ans.append(even[0])
                even.remove(even[0])
        return ans

            
        