class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res=set()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            sum1 = 0-nums[i]
            while j<k:
                if nums[j]+nums[k]==sum1:
                    res.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif nums[j]+nums[k]>sum1:
                    k-=1
                else:
                    j+=1
        return list(res)