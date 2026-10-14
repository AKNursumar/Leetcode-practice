# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        res = []
        def dfs(root):
            if not root:
                res.append('null')
                return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(p)
        dfs(q)
        return res[:len(res)//2] == res[len(res)//2:]
        
        