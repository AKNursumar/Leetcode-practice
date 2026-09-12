class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        xor = 0
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                xor ^=num
        return xor
        