class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=0
        hashmap={}
        for r in range(len(nums)):
            hashmap[nums[r]]=1+hashmap.get(nums[r],0)
            if hashmap[nums[r]]>1 and r-l<=k:
                return True
            if r-l+1>k:
                hashmap[nums[l]]-=1
                l+=1
        return False
            
            