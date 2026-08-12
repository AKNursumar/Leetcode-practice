# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sys.set_int_max_str_digits(10000)
        n = ""
        while head:
            n += str(head.val) 
            head = head.next
        n = str(int(n)*2)
        dummy = ListNode(0,None)
        curr = dummy
        for ch in n:
            curr.next = ListNode(int(ch))
            curr = curr.next
        return dummy.next

        