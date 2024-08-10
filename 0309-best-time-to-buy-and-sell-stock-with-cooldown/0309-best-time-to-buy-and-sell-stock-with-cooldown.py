class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def dfs(i,buying):
            if (i,buying) in cache:
                return cache[(i,buying)]
            if i>=len(prices):
                return 0
            if buying:
                buy = dfs(i+1, 0) - prices[i]
                cooldown = dfs(i+1,buying)
                cache[(i,buying)] = max(buy,cooldown)
            else:
                sell = dfs(i+2,1) + prices[i]
                cooldown = dfs(i+1,buying)
                cache[(i,buying)] = max(sell,cooldown)
            return cache[(i,buying)]
        return dfs(0,1)

