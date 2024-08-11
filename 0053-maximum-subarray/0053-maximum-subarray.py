class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #greedy 
        max1=float("-inf")
        curSum = 0
        for j in range(0,len(nums)):
            curSum+=nums[j]
            max1 = max(curSum,max1)
            if curSum<0:
                curSum = 0
                
        return max1
