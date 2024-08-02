# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root==None:
                return [0,0]
            left=dfs(root.left)
            right=dfs(root.right)
            withRoot = root.val  + left[1] + right[1]
            withoutroot = max(left)+max(right)
            return [withRoot,withoutroot]
        return max(dfs(root))