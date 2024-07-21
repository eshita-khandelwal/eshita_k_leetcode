class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            grid[i][j]='0'
            if i+1<n and grid[i+1][j]=='1':
                dfs(i+1,j)
            if i-1>=0 and grid[i-1][j]=='1':
                dfs(i-1,j)
            if j+1<m and grid[i][j+1]=='1':
                dfs(i,j+1)
            if j-1>=0 and grid[i][j-1]=='1':
                dfs(i,j-1)

            
        n = len(grid)
        m = len(grid[0])
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1':
                    dfs(i,j)
                    res+=1
        return res

