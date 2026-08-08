# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        s = ""
        while head:
            s = str(head.val)+s
            head = head.next
        res = 0
        for i in range(0,len(s)):
            res +=(2**i * int(s[i]))
        return res




        