# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ""
        s2 = ""
        sum1 = 0
        while l1:
            s1 = str(l1.val)+s1
            l1 = l1.next
        while l2:
            s2 = str(l2.val)+s2
            l2 = l2.next
        sum1 = str(int(s1)+int(s2))[::-1]
        dummy = ListNode()
        curr = dummy
        for i in range(len(sum1)):
            curr.next = ListNode(int(sum1[i]))
            curr = curr.next
        return dummy.next
        