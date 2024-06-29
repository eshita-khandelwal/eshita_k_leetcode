class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = nums[0]
        for i in range(1,len(nums)):
            x^=nums[i]
        return x