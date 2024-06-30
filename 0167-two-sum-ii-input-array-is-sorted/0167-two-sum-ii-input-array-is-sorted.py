class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        result=[]
        i=0
        j=len(nums)-1
        while i<j:
            if nums[i]+nums[j]==target:
                result.append(i+1)
                result.append(j+1)
                break
            elif nums[i]+nums[j]>target:
                j-=1
            else:
                i+=1
        
        return result

