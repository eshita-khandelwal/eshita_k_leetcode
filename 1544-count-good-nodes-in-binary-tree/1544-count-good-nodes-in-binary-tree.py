# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,maxv):
        if root==None:
            return 0
        res=0
        if root.val>=maxv:
            maxv = max(maxv,root.val)
            return 1 + self.dfs(root.left,maxv) + self.dfs(root.right,maxv)
        return  self.dfs(root.left,maxv) + self.dfs(root.right,maxv)
    def goodNodes(self, root: TreeNode) -> int:
        
        return self.dfs(root,root.val)
