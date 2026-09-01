# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        ind = 0
        ind_arr = []
        prev = head
        curr = head.next
        if not head.next.next:
            return [-1,-1]
        while curr.next:
            ind +=1
            if (curr.val<prev.val and curr.val<curr.next.val) or (curr.val>prev.val and curr.val>curr.next.val):
                ind_arr.append(ind)
            prev = curr
            curr = curr.next
        if len(ind_arr)==0 or len(ind_arr)==1:
            return [-1,-1]
        diff = float("inf")
        for i in range(1,len(ind_arr)):
            diff = min(diff,ind_arr[i]-ind_arr[i-1])
        return [diff,ind_arr[-1]-ind_arr[0]]


        