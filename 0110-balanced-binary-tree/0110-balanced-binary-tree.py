# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #return [true/false,height of the tree]
        def height(root):
            if root==None:
                return [True,0]
            l = height(root.left)
            r = height(root.right)
            balance = l[0] and r[0] and abs(l[1]-r[1])<=1
            return [balance,1+max(l[1],r[1])]
        
        return height(root)[0]