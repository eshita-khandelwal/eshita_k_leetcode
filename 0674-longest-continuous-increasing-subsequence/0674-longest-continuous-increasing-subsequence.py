class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res=1
        for i in range(len(nums)-1):
            cnt = 1
            cmp = nums[i]#the number to compare ifrst will be nums[i] then we keep it setting to the currrent number 
            for j in range(i+1,len(nums)):
                if nums[j]>cmp:
                    cnt+=1
                    cmp = nums[j]
                else:
                    break
            res=max(res,cnt)
        return res