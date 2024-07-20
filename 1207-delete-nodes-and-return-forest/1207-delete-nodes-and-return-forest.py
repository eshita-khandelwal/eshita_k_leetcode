# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        s = set(to_delete)
        def dfs(root,flag): #flag says if we have to store the root or not
            if root == None:
                return None
            todel = root.val in s
            root.left = dfs(root.left,todel)
            root.right = dfs(root.right,todel)
            if not todel and flag: 
                res.append(root)
            if todel:
                return None
            return root
        dfs(root,True)
        return res
