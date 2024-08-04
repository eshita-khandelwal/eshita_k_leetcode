class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sum1 = set()
        for i in range(len(nums)-1):
            s = nums[i]+nums[i+1]
            if s in sum1:
                return True
            sum1.add(s)

        return False