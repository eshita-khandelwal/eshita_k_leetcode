class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = {}
        res=0
        oddc = 0
        for i in range(len(nums)):
            if nums[i]%2==1:
                oddc+=1
            count[oddc] = 1 + count.get(oddc,0)
        if k in count:
            res = count[k] 
        for cnt,val in count.items():
            if cnt+k in count:
                res+=count[cnt] * count[cnt+k]
        return res
