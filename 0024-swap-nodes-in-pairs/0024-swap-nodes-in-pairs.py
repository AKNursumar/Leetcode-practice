# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        n1 = ListNode()
        prev = n1
        prev.next = head
        curr = prev.next
        next_p = curr.next
        while next_p:
            prev.next = prev.next.next
            curr.next = curr.next.next
            next_p.next = curr
            prev = curr
            curr = curr.next
            if curr:
                next_p = curr.next
            else:
                break
        return n1.next