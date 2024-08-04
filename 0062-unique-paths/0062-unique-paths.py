class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #to reach the finish point finish point will need 1 way to do that so we assign it to 0
        #the last row or last col also has one way each to go and reach finish point as we can only move right or move down. we cannot move left or up. so assign them to 1. each inside boxes have ways -> or down. so we jsut add the ways and return dp[0][0]
        dp = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if i == n-1 or j == m-1:
                    dp[i][j]=1
                else:
                    dp[i][j] = dp[i+1][j]+dp[i][j+1]
        print(dp)
        return dp[0][0]