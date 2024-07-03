class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp=prices[0]
        maxprofit = 0
        for i in range(len(prices)):
            minp=min(prices[i],minp)
            maxprofit=max(maxprofit,prices[i]-minp)
        return maxprofit
        