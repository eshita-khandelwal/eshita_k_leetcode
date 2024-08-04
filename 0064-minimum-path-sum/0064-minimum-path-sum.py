class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if i+1<n and j+1<m:
                    dp[i][j] = grid[i][j] + min(dp[i+1][j],dp[i][j+1])
                else:
                    if i+1==n and j+1==m:
                        dp[i][j] = grid[i][j]
                    elif i+1==n:
                        dp[i][j] = grid[i][j] + dp[i][j+1]
                    elif j+1==m:
                        dp[i][j] = grid[i][j] + dp[i+1][j]
        return dp[0][0]
