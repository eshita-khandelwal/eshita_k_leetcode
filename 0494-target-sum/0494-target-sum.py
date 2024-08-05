class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # n = len(nums)
        #dp = [[0 for _ in range(n+1)]for _ in range(2*sum(nums)+1)]
        cache={}
        def tsum(i,s):
            if (i,s) in cache:
                return cache[(i,s)]
            if i==len(nums):
                if s==target:
                    cache[(i,s)]=1
                    return 1
                cache[(i,s)]=0
                return 0
            
            takep = tsum(i+1,s+nums[i])
            taken = tsum(i+1,s-nums[i])
            cache[(i,s)]=takep+taken
            return takep+taken
        return tsum(0,0)
       