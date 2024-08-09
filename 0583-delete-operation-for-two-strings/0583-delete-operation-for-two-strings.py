class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #delete operation will be (i+1,j) or (i,j+1)
        dp = [[float("inf") for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        for j in range(len(word2)+1):
            dp[len(word1)][j] = len(word2)-j
        for i in range(len(word1)+1):
            dp[i][len(word2)]=len(word1)-i
        
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i]==word2[j]:
                    dp[i][j]=dp[i+1][j+1]
                else:
                    dp[i][j] = 1+ min(dp[i][j+1],dp[i+1][j])
        return dp[0][0]