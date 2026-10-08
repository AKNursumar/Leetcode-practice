# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        curr = head
        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next
        n = len(nodes)
        twin = 0
        m = float("-inf")
        for i in range(n//2):
            twin = nodes[i].val + nodes[n-i-1].val
            m = max(m,twin)
        return m
        