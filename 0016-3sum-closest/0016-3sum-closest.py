class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j<k:
                guess = nums[i]+nums[j]+nums[k]
                if abs(guess-target)<abs(ans-target):
                    ans=guess
                if guess<target:
                    j+=1
                elif guess>target:
                    k-=1
                else:
                    return target
        
        return ans
