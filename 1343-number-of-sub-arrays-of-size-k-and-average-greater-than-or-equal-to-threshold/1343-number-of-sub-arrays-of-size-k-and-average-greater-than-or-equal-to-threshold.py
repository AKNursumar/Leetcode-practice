class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        c = 0
        t_sum = threshold*k
        curr = sum(arr[:k])
        if curr >= t_sum:
            c+=1
        for i in range(1,len(arr)-k+1):
            curr = curr - arr[i-1] + arr[i+k-1]
            if curr >= t_sum:
                c+=1
        return c
        