class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(curr_o,curr_c,curr):
            if curr_o==n and curr_c==0 and len(curr)==2*n:
                res.append(curr)
            if curr_o<n:
                dfs(curr_o+1,curr_c+1,curr+'(')
            if curr_c>0:
                dfs(curr_o,curr_c-1,curr+')')
        
        res=[]
        dfs(0,0,"")
        return res