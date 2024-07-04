class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r=0,len(nums)-1
        
        while l<=r:
            if nums[l]<=nums[r]:
                res = min(res,nums[l])
                return res
            mid = (l+r)//2
            res = min(res,nums[mid])
            if nums[l]<=nums[mid]:
                l = mid+1
            else:
                r = mid-1
        return res

