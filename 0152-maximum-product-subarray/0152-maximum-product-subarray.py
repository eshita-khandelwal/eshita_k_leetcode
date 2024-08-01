class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        curMin,curMax = 1,1
        for n in nums:
            if n==0:
                curMin,curMax = 1,1
            temp = curMax
            curMax = max(curMax*n,curMin*n,n)
            curMin = min(temp*n,curMin*n,n)
            res= max(res,curMax)
        return res