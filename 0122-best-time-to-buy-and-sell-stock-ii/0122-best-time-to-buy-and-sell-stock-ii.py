class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def dfs(i,buying):
            if (i,buying) in cache:
                return cache[(i,buying)]
            if i==len(prices):
                return 0
            if buying:
                sell = dfs(i+1,0) - prices[i]
                notsell = dfs(i+1,buying)
                cache[(i,buying)] = max(sell,notsell)
                return cache[(i,buying)]
            else:
                buy = dfs(i+1,1) + prices[i]
                notbuy = dfs(i+1,buying)
                cache[(i,buying)] = max(buy,notbuy)
                return cache[(i,buying)]
        return dfs(0,1)
            