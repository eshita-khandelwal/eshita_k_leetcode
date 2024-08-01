class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def house(num):
            dp = [0]*len(num)
            dp[0] = num[0]
            if len(num)==1:
                return num[0]
            dp[1]=max(num[0],num[1])
            for i in range(2,len(num)):
                dp[i]=max(dp[i-1],dp[i-2]+num[i])
            return dp[len(num)-1]
        n = len(nums)
        if n==1:
            return nums[0]
        a = house(nums[0:n-1])
        b = house(nums[1:n])
        return max(a,b)