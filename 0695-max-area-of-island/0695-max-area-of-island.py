class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i<0 or j<0 or i==n or j==m or grid[i][j]==0:
                return 0
            grid[i][j]=0
            return dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)+1
        
        maxarea = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    a = dfs(i,j)
                    maxarea=max(a,maxarea)
        return maxarea