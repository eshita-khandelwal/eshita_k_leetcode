class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp=[amount+1]*(amount+1)
        # dp[0]=0
        
        # for a in range(1,amount+1):
        #     for c in coins:
        #         if a-c>=0:
        #             dp[a]=min(dp[a],1+dp[a-c])
        # return dp[amount] if dp[amount]!=amount+1 else -1
        res = float("inf")
        cache = {}
        def dfs(i,a):
            if (i,a) in cache:
                return cache[(i,a)]
            if a==amount:
                return 0
            if i>=len(coins):
                return 10**8
            if a>amount:
                return 10**8
            cache[(i,a)]= min(1+dfs(i,a+coins[i]),dfs(i+1,a))
            return cache[(i,a)]
        ans = dfs(0,0)
        if amount==0:
            return 0
        return ans if ans!=10**8 else -1   
