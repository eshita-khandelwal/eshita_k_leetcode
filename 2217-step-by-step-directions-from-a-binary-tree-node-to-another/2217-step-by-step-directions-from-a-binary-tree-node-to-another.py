# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        #https://www.youtube.com/watch?v=JegJNGcwtFg
        #path is a string 
        def dfs(root,path,target):
            if root==None:
                return ""
            if root.val == target:
                return path
            path.append("L")
            res = dfs(root.left,path,target)
            if res: return res
            path.pop()
            path.append("R")
            res = dfs(root.right,path,target)
            if res: return res
            path.pop()
            
            return ""

        
        s1 = dfs(root,[],startValue)
        s2 = dfs(root,[],destValue)
        i=0
        while i<min(len(s1),len(s2)):
            if s1[i]!=s2[i]:
                break
            i+=1
        r = ['U'] * len(s1[i:]) + s2[i:]
        return "".join(r)
            