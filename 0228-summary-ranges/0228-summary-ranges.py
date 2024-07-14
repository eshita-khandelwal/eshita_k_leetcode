class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]
        r=[]
        if len(nums)==0:
            return []
        a=nums[0]
        for i in range(0,len(nums)):
            if i+1<len(nums) and nums[i+1]==1+ nums[i]:
                continue
            else:
                if a==nums[i]:
                    res.append(str(a))
                else:
                    res.append(str(a)+"->"+str(nums[i]))
                if i+1<len(nums):
                    a=nums[i+1]
        
        return res
