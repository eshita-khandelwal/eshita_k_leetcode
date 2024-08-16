class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #pointers for this question: avoid 0 becasue it will make things bad, by resetting values of curmin and curmax to 1. maintain min,max at each i because there can be negative numbers too. 
        res = float("-inf")
        curmin = 1
        curmax = 1
        for i in nums:
            if i==0:
                curmin,curmax = 1,1
            temp = curmax * i
            curmax = max(i,temp,curmin*i)
            curmin = min(i,temp,curmin*i)
            res = max(res,curmax)
        return res