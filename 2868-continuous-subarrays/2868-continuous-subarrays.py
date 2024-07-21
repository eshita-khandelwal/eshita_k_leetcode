class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        m = {}
        l = 0
        res = 0
        for r in range(len(nums)):
            m[nums[r]]=r
            for k in list(m):
                if abs(nums[r]-k)>2:
                    l = m.pop(k)+1
            res+=r-l+1
        return res