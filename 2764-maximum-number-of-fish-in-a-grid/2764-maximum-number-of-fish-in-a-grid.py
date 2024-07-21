class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i==n or j==m or i<0 or j<0 or grid[i][j]==0:
                return 0
            temp = grid[i][j]
            grid[i][j]=0
            return dfs(i+1,j) + dfs(i,j+1) + dfs(i-1,j) + dfs(i,j-1)+ temp
            
        n = len(grid)
        m = len(grid[0])
        max1=0
        for i in range(n):
            for j in range(m):
                ans=0
                if grid[i][j]!=0:
                    x = dfs(i,j)
                    max1=max(max1,x)
        return max1