# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        val = []
        s = 0
        curr = head.next
        while curr:
            if curr.val == 0:
                val.append(s)
                s = 0
            else:
                s +=curr.val
            curr = curr.next
        head = ListNode(val[0])
        curr = head
        for i in range(1,len(val)):
            curr.next = ListNode(val[i])
            curr = curr.next
        return head
        