class Solution:
    def maxLength(self, nums: List[int]) -> int:
        l = len(nums)
        pro = 1
        lcm = 0
        gcd = 0
        j = 0
        m = 0
        while j!=l:
            n = l
            while n>=j:
                pro = math.prod(nums[j:n])
                lcm = math.lcm(*nums[j:n])
                gcd = math.gcd(*nums[j:n])
                if pro == lcm*gcd:
                    m=max(m,n-j)
                n-=1
            j+=1
        
        return m

        