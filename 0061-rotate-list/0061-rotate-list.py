# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,nodes:list,l,r):
        while l<=r:
            nodes[l].val,nodes[r].val = nodes[r].val,nodes[l].val
            l+=1
            r-=1
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if k==0 or not head:
            return head
        curr = head
        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next
        k = k%len(nodes)
        self.reverse(nodes,0,len(nodes)-1)
        self.reverse(nodes,0,k-1)
        self.reverse(nodes,k,len(nodes)-1)
        return head