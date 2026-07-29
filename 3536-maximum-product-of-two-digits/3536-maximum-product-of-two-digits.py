class Solution:
    def maxProduct(self, n: int) -> int:
        # arr = []
        # while(n>0):
        #     arr.append(n%10)
        #     n = n//10
        # arr.sort()
        # return arr[len(arr)-1]*arr[len(arr)-2]
        s1 = str(n)
        arr = []
        for ch in s1:
            arr.append(int(ch))
        arr.sort()
        return arr[len(arr)-1]*arr[len(arr)-2]

        