# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if root==None:
            return res
        q=deque()
        q2=deque()
        q2.append([root.val,1])
        l=1
        q.append([root,1])
        while q:
            cur = q.popleft()

            l=cur[1]+1
            #print(q)
            if cur[0].right:
                q.append([cur[0].right,l])
                q2.append([cur[0].right.val,l])
            if cur[0].left:
                q.append([cur[0].left,l])
                q2.append([cur[0].left.val,l])
        
        x=1
       
        while q2:
            cur = q2.popleft()
            level = cur[1]
          
            if level==x:
                res.append(cur[0])
                x+=1
        return res           
                
            
            

