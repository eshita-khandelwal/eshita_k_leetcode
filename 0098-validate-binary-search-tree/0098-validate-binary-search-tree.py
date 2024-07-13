# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res=[]
        def isValid(root):
            if root==None:
                return
            isValid(root.left)
            res.append(root.val)
            isValid(root.right)
        
        isValid(root)
        for i in range(len(res)-1):
            if res[i]>=res[i+1]:
                return False
        return True
        
        