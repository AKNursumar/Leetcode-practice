# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr = list1
        i = a
        while i>1:
            curr = curr.next
            i-=1
        n_p = curr.next
        curr.next = list2
        for i in range(b-a+1):
            n_p = n_p.next
        while curr.next:
            curr = curr.next
        curr.next = n_p
        return list1
        
        