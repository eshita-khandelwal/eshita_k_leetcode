class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        #solve longest common sequence first to solve this problem. 
        #the idea is that i will have one more string reverse of our given string and then find common characters.
        rs = s[::-1]
        dp = [[0 for _ in range(len(rs)+1)] for _ in range(len(s)+1)]
        for i in range(len(s)-1,-1,-1):
            for j in range(len(rs)-1,-1,-1):
                if s[i]==rs[j]:
                    dp[i][j]=1+dp[i+1][j+1]
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
        return dp[0][0]