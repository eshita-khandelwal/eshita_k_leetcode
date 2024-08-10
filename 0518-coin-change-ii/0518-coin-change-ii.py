class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dfs(i,a):
            if (i,a) in cache:
                return cache[(i,a)]
            if a==amount:
                return 1
            if i>=len(coins) or a>amount:
                return 0
            cache[(i,a)] = dfs(i,a+coins[i])+dfs(i+1,a)
            return cache[(i,a)]
        return dfs(0,0)
            