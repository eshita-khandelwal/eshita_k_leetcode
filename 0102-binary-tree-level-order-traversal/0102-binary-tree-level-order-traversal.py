# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        q=deque()
        q.append([root,1])
        res=[]
        q2=deque()
        q2.append([root.val,1])
        while q:
            cur =q.popleft()
            l=cur[1]+1
            if cur[0].left:
                q.append([cur[0].left,l])
                q2.append([cur[0].left.val,l])
            if cur[0].right:
                q.append([cur[0].right,l])
                q2.append([cur[0].right.val,l])
        i=0
        l=1
        r = list(q2)
        while i<len(r):
            temp=[]
            while i<len(r) and l == r[i][1]:
                temp.append(r[i][0])
                i+=1
            res.append(temp)
            l+=1
        return res
            

        

            