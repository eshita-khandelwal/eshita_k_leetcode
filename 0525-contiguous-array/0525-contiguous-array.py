class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res=0
        count={}
        zero=0
        one=0
        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
            else:
                one+=1
            if zero-one==0:
                res=zero+one
            else:
                if zero-one in count:
                    res=max(res,i-count[zero-one]) #we do this because between these indices we got our perfect 0 number which we need. 
                else:
                    count[zero-one]=i #storing it so we know when was the first time we encountereed it. do not update the first occurance because we want to find the maximum length
        
        return res
