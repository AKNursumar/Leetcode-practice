class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        c = 0
        a = 0
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])<=d:
                    break
                a+=1
            if a==len(arr2):
                c+=1
            a = 0
            
        return c

        