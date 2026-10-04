# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        nodes[k-1].val,nodes[-k].val = nodes[-k].val,nodes[k-1].val
        return head

        
        