class Solution:
    def rob(self, nums: List[int]) -> int:
        #we can have choosen house1 or house 2 at the start
        n = len(nums)
        dp = [0 for i in range(n)]
        dp[0]=nums[0]
        if n==1:
            return nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        return dp[n-1]