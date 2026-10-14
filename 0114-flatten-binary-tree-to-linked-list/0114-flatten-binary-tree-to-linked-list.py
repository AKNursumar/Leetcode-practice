# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        def dfs(root):
            if root == None:
                return
            res.append(root)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        curr = root
        for i in range(1,len(res)):
            curr.right = res[i]
            curr.left = None
            curr = curr.right
