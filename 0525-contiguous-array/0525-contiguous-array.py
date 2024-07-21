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
                    res=max(res,i-count[zero-one])
                else:
                    count[zero-one]=i
        
        return res
