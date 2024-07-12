# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=[0]
        def dfs(root):
            if root==None:
                return -1
            l = dfs(root.left)
            r = dfs(root.right)
            res[0]=max(res[0],l+r+2)
            return 1 + max(l,r)
        
        dfs(root)
        return res[0]
        
