# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:

        arr = []
        for i in range(len(lists)):
            head = lists[i]
            while head:
                arr.append(head.val)
                head = head.next
        arr.sort()

        dummy = ListNode()
        curr = dummy
        for i in range(len(arr)):
            new = ListNode(arr[i])
            curr.next = new
            curr = curr.next
        return dummy.next
        