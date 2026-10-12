# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        stack = []
        curr = head
        while curr:
            if not stack:
                stack.append(curr)
            else:
                if stack[-1].val > curr.val:
                    stack.append(curr)
                else:
                    while stack and stack[-1].val < curr.val:
                        stack.pop()
                    stack.append(curr)
            curr = curr.next
        head_new = stack[0]
        curr_new = head_new
        for i in range(1,len(stack)):
            curr_new.next = stack[i]
            curr_new = curr_new.next
        return head_new
        