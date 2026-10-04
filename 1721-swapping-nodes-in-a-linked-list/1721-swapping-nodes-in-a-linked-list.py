# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = head
        r = head
        curr = head
        total = 0
        while curr:
            curr = curr.next
            total +=1
        k_r = total-k+1
        while k>1:
            l = l.next
            k-=1
        while k_r>1:
            r = r.next
            k_r -=1
        l.val,r.val = r.val,l.val
        return head
        

        
        