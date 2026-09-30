# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == headB:
            return headA
        stackA = []
        stackB = []
        while headA:
            stackA.append(headA)
            headA = headA.next
        while headB:
            stackB.append(headB)
            headB = headB.next
        prev = None
        while stackA and stackB:
            node1 = stackA.pop()
            node2 = stackB.pop()
            if node1 == node2:
                prev = node1
            else:
                return prev
        if stackA or stackB:
            return prev
            
            