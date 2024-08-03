class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        #we are using pair key:i and value is [LIS,COUNT]. this is for every i from 0 to len(nums)
        dp={}
        maxLis,res=0,0

        for i in range(len(nums)-1,-1,-1):
            maxlen,cnt=1,1
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    l,c=dp[j]
                    if l+1>maxlen:
                        maxlen,cnt = l+1,c
                    elif l+1==maxlen:
                        cnt+=c
            dp[i]=[maxlen,cnt]
            if maxlen>maxLis:
                maxLis,res=maxlen,cnt
            elif maxlen==maxLis:
                res+=cnt
        
        return res
