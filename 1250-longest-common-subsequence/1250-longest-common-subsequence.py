class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
       #we are going bottom up. compute the last characters and work our way upwards. the idea is abcde and ace here e and e match so we reduce the length of both string by 1 abcd and ac clearly d and c dont match so we compare (abcd and a  ) and (abc and ac). we use 2d dp matrix so compute this. if the characters match we do 1+ diagonal or else we do max(dp[i+1][j],dp[i][j+1]). we initialise the last row and col by 0 because if the string goes out of bound that means no common subsequence 
        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]

        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i]==text2[j]:
                    dp[i][j] = dp[i+1][j+1]+1
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
        return dp[0][0]
        


